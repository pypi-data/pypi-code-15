"""
This module defines a device-independent MultiChannel Analyzer (MCA) class.

Authors/Modifications:
----------------------
* Mark Rivers, GSECARS
* Modified for Tdl, tpt
* modified and simplified for Larch, M Newville
"""
import six
import numpy as np
from larch import Group, isgroup

from larch_plugins.xrf.deadtime import calc_icr, correction_factor
from larch_plugins.xrf.roi import ROI

def isLarchMCAGroup(grp):
    """tests whether variable holds a valid Larch MCAGroup"""
    return isgroup(grp, 'energy',  'counts', 'rois')

class Environment:
    """
    The "environment" or related parameters for a detector.  These might include
    things like motor positions, temperature, anything that describes the
    experiment.

    Attributes:
    -----------
    * name         # A string name of this parameter, e.g. "13IDD:m1"
    * description  # A string description of this parameter, e.g. "X stage"
    * value        # A string value of this parameter,  e.g. "14.223"
    """
    def __init__(self, desc='', addr='', val=''):
        self.addr  = addr.strip()
        self.val   = val.strip()
        self.desc  = desc.strip()
        if self.desc.startswith('(') and self.desc.endswith(')'):
            self.desc = self.desc[1:-1]

    def __repr__(self):
        return "Environment(desc='%s', val='%s', addr='%s')" % (self.desc,
                                                                self.val,
                                                                self.addr)


class MCA(Group):
    """
    MultiChannel Analyzer (MCA) class

    Attributes:
    -----------
    * self.name        = 'mca'  # Name of the mca object
    * self.nchans      = 2048   # number of mca channels
    * self.counts      = None   # MCA data

    # Counting parameters
    * self.start_time   = ''    # Start time and date, a string
    * self.live_time    = 0.    # Elapsed live time in seconds
    * self.real_time    = 0.    # Elapsed real time in seconds
    * self.read_time    = 0.    # Time that the MCA was last read in seconds
    * self.total_counts = 0.    # Total counts between the preset start and stop channels
    * self.input_counts = 0.    # Actual total input counts (eg given by detector software)
                                # Note total_counts and input counts ARE NOT time normalized
                                #
    * self.tau          = -1.0  # Factor for deadtime/detector saturation calculations, ie
                                #     ocr = icr * exp(-icr*tau)
    * self.icr_calc     = -1.0  # Calculated input count rate from above expression
    * self.dt_factor   = 1.0    # deadtime correction factor based on icr,ocr,lt,rt
                                # data_corrected = data * dt_factor
                                #
    # Calibration parameters
    * self.offset       = 0.    # Offset
    * self.slope        = 1.0   # Slope
    * self.quad         = 0.    # Quadratic

    Notes:
    ------
    If input_counts are read from the data file then there is no need for tau
    values (and hence icr_calc is not used) - ie we assume the detector
    provides the icr value.

    The application of corrections uses the following logic:
       if tau > 0 this will be used in the correction factor calculation
       if tau = 0 then we assume ocr = icr in the correction factor calculation
       if tau < 0 (or None):
       if input_counts > 0 this will be used for icr in the factor calculation
          if input_counts <= 0 we assume ocr = icr in the correction factor calculation

    Energy calibration is based on the following:
        energy = offset + slope*channel + quad*channel**2

    """
    ###############################################################################
    def __init__(self, counts=None, nchans=2048, start_time='',
                 offset=0, slope=0, quad=0, name='mca', dt_factor=1,
                 real_time=0, live_time = 0, input_counts=0, tau=0, **kws):

        self.name    = name
        self.nchans  = nchans
        self.environ = []
        self.rois    = []
        self.counts  = counts

        # Calibration parameters
        self.offset       = offset # Offset
        self.slope        = slope  # Slope
        self.quad         = quad   # Quadratic

        # Counting parameters
        self.start_time   = start_time
        self.real_time    = real_time  # Elapsed real time in seconds (requested counting time)
        self.live_time    = live_time  # Elapsed live time in seconds (time detector is live)
        self.input_counts = input_counts # Actual total input counts (eg given by detector software)
                                  # Note total_counts and input counts ARE NOT time normalized
                                  #
        self.total_counts = 0.    # Total counts between the preset start and stop channels
        self.tau          = tau   # Factor for deadtime/detector saturation calculations, ie
                                  #     ocr = icr * exp(-icr*tau)
        # Calculated correction values
        self.icr_calc    = -1.0  # Calculated input count rate from above expression
        # corrected_counts = counts * dt_factor
        self.bgr = None
        self.dt_factor   = float(dt_factor)
        if counts is not None:
            self.nchans      = len(counts)
            self.total_counts =  counts.sum()
        self.get_energy()
        self._calc_correction()
        Group.__init__(self)

    def __repr__(self):
        form = "<MCA %s, nchans=%d, counts=%d, realtime=%.1f>"
        return form % (self.name, self.nchans, self.total_counts, self.real_time)

    def add_roi(self, name='', left=0, right=0, bgr_width=3,
                counts=None, sort=True):
        """add an ROI"""
        name = name.strip()
        roi = ROI(name=name, left=left, right=right,
                  bgr_width=bgr_width, counts=counts)

        rnames = [r.name.lower() for r in self.rois]
        if name.lower() in rnames:
            iroi = rnames.index(name.lower())
            self.rois[iroi] = roi
        else:
            self.rois.append(roi)
        if sort:
            self.rois.sort()

    def get_roi_counts(self, roi, net=False):
        """get counts for an roi"""
        thisroi = None
        if isinstance(roi, ROI):
            thisroi = roi
        elif isinstance(roi, int) and roi < len(self.rois):
            thisroi = self.rois[roi]
        elif isinstance(roi, six.string_types):
            rnames = [r.name.lower() for r in self.rois]
            for iroi, nam in enumerate(rnames):
                if nam.startswith(roi.lower()):
                    thisroi = self.rois[iroi]
                    break
        if thisroi is None:
            return None
        return thisroi.get_counts(self.counts, net=net)

    def add_environ(self, desc='', val='', addr=''):
        """add an Environment setting"""
        if len(desc) > 0 and len(val) > 0:
            self.environ.append(Environment(desc=desc, val=val, addr=addr))

    def update_correction(self, tau=None):
        """
        Update the deadtime correction

        if tau == None just recompute,
        otherwise assign a new tau and recompute
        """
        if tau is not None:
            self.tau = tau
        self._calc_correction()

    def _calc_correction(self):
        """
        if self.tau > 0 this will be used in the correction factor calculation
        if self.tau = 0 then we assume ocr = icr in the correction factor calculation,
                      ie only lt correction
                     (note deadtime.calc_icr handles above two conditions)
        if self.tau < 0 (or None):
           if input_counts > 0  this will be used for icr in the factor calculation
           if input_counts <= 0 we assume ocr = icr in the correction factor calculation,
                                ie only lt correction
        """
        if self.live_time <= 0 or self.real_time <= 0:
            self.dt_factor  = 1.0
            return

        if self.total_counts > 0:
            ocr = self.total_counts / self.live_time
        else:
            ocr = None

        if self.tau >= 0:
            icr = calc_icr(ocr,self.tau)
            if icr is None:
                icr = 0
            self.icr_calc = icr
        elif self.input_counts > 0:
            icr = self.input_counts / self.live_time
        else:
            icr = ocr = None
        self.dt_factor  = correction_factor(self.real_time, self.live_time,
                                             icr=icr,  ocr=ocr)
        if self.dt_factor <= 0:
            print( "Error computing counts correction factor --> setting to 1")
            self.dt_factor = 1.0

    ########################################################################
    def get_counts(self, correct=True):
        """
        Returns the counts array from the MCA

        Note if correct == True the corrected counts is returned. However,
        this does not (re)compute the correction factor, therefore, make
        sure the correction factor is up to date before requesting
        corrected counts...
        """
        if correct:
            return  (self.dt_factor * self.counts).astype(np.int)
        else:
            return self.counts

    def get_energy(self):
        """
        Returns array of energy for each channel in the MCA spectra.
        """
        chans = np.arange(self.nchans, dtype=np.float)
        self.energy = self.offset +  chans * (self.slope + chans * self.quad)
        return self.energy

    def save_columnfile(self, filename, headerlines=None):
        "write summed counts to simple ASCII column file for mca counts"
        f = open(filename, "w+")
        f.write("#XRF counts for %s\n" % self.name)
        if headerlines is not None:
            for i in headerlines:
                f.write("#%s\n" % i)
        f.write("#\n")
        f.write("#EnergyCalib.offset = %.9g \n" % self.offset)
        f.write("#EnergyCalib.slope = %.9g \n" % self.slope)
        f.write("#EnergyCalib.quad  = %.9g \n" % self.quad)
        f.write("#Acquire.RealTime  = %.9g \n" % self.real_time)
        f.write("#Acquire.LiveTime  = %.9g \n" % self.live_time)
        roiform = "#ROI_%i '%s': [%i, %i]\n"
        for i, r in enumerate(self.rois):
            f.write(roiform % (i+1, r.name, r.left, r.right))

        f.write("#-----------------------------------------\n")
        f.write("#    energy       counts     log_counts\n")

        for e, d in zip(self.energy, self.counts):
            dlog = 0.
            if  d > 0: dlog = np.log10(max(d, 1))
            f.write(" %10.4f  %12i  %12.6g\n" % (e, d, dlog))
        f.write("\n")
        f.close()

    def save_mcafile(self, filename):
        """write MCA file

        Parameters:
        -----------
        * filename: output file name
        """
        fp = open(filename, 'w')
        fp.write('VERSION:    3.1\n')
        fp.write('ELEMENTS:   1\n')
        fp.write('DATE:       %s\n' % self.start_time)
        fp.write('CHANNELS:   %i\n' % len(self.counts))
        fp.write('REAL_TIME:  %f\n' % self.real_time)
        fp.write('LIVE_TIME:  %f\n' % self.live_time)
        fp.write('CAL_OFFSET: %e\n' % self.offset)
        fp.write('CAL_SLOPE:  %e\n' % self.slope)
        fp.write('CAL_QUAD:   %e\n' % self.quad)

        # Write ROIS  in channel units
        fp.write('ROIS:      %i\n' % len(self.rois))
        for i, roi in enumerate(self.rois):
            fp.write('ROI_%i_LEFT:  %i\n' % (i, roi.left))
            fp.write('ROI_%i_RIGHT:  %i\n' % (i, roi.right))
            fp.write('ROI_%i_LABEL: %s &\n' % (i, roi.name))

        # environment
        for e in self.environ:
            fp.write('ENVIRONMENT: %s="%s" (%s)\n' % (e.addr, e.val, e.desc))

        # data
        fp.write('DATA: \n')
        for d in self.counts:
            fp.write(" %s\n" % d)
        fp.close()

def create_mca(counts=None, nchans=2048, offset=0, slope=0, quad=0,
               name='mca', start_time='', real_time=0, live_time=0,
               dt_factor=1, input_counts=0, tau=0, _larch=None, **kws):

    """create an MCA object, containing an XRF (or similar) spectrum

     Parameters:
     ------------
      counts:   counts array
      nchans:   # channels

     Returns:
     ----------
      an MCA object

    """
    return MCA(counts=counts, nchans=nchans, name=name,
               start_time=start_time, offset=offset, slope=slope,
               quad=quad, dt_factor=dt_factor, real_time=real_time,
               live_time=live_time, input_counts=input_counts,
               tau=tau, **kws)

def registerLarchPlugin():
    return ('_xrf', {'create_mca': create_mca})
