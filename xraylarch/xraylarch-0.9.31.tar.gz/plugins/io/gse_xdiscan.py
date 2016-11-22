#!/usr/bin/env python

import os
import sys
import copy
import time
import gc

import numpy as np
from larch import Group, ValidateLarchPlugin, use_plugin_path
from larch.utils import OrderedDict

from larch_plugins.io import XDIFile, XDIFileException, iso8601_time

use_plugin_path('xrmmap')
from xsp3_hdf5 import XSPRESS3_TAUS, estimate_icr

@ValidateLarchPlugin
def read_gsexdi(fname, _larch=None, nmca=4, bad=None, **kws):
    """Read GSE XDI Scan Data to larch group,
    summing ROI data for MCAs and apply deadtime corrections
    """
    group = _larch.symtable.create_group()
    group.__name__ ='GSE XDI Data file %s' % fname
    xdi = XDIFile(str(fname))

    group._xdi = xdi
    group.filename = fname
    group.npts = xdi.npts
    group.bad_channels = bad
    group.dtc_taus = XSPRESS3_TAUS
    if _larch.symtable.has_symbol('_sys.gsecars.xspress3_taus'):
        group.dtc_taus = _larch.symtable._sys.gsecars.xspress3_taus

    for family in ('scan', 'mono', 'facility'):
        for key, val in xdi.attrs.get(family, {}).items():
            if '||' in val:
                val, addr = val.split('||')
            try:
                val = float(val)
            except:
                pass
            setattr(group, "%s_%s" % (family, key), val)

    ocrs, icrs = [], []
    ctime = None
    for attrname in dir(xdi):
        if attrname.lower() == 'counttime':
            ctime = getattr(xdi, attrname)
    if ctime is None:
        try:
            ctime = xdi.TSCALER / 5.e7
        except AttributeError:
            ctime = 1.0

    is_xspress3 = any(['13QX4' in a[1] for a in xdi.attrs['column'].items()])
    group.with_xspress3 = is_xspress3
    for i in range(nmca):
        ocr = getattr(xdi, 'OutputCounts_mca%i' % (i+1), None)
        if ocr is None:
            ocr = ctime
        ocr = ocr/ctime
        icr = getattr(xdi, 'InputCounts_mca%i' % (i+1), None)
        if icr is not None:
            icr = icr/ctime
        else:
            icr = 1.0*ocr
            if is_xspress3:
                tau = group.dtc_taus[i]
                icr = estimate_icr(ocr*1.00, tau, niter=7)
        ocrs.append(ocr)
        icrs.append(icr)
    labels = []
    sums = OrderedDict()
    for i, arrname in enumerate(xdi.array_labels):
        dat = getattr(xdi, arrname)
        aname = sumname = rawname = arrname.lower()
        if ('_mca' in aname and 'outputcounts' not in aname and
            'clock' not in aname):
            sumname, imca = sumname.split('_mca')
            imca = int(imca) - 1
            datraw = dat*1.0
            rawname = sumname + '_nodtc'
            dat   = dat * icrs[imca]/ ocrs[imca]
            if any(np.isnan(dat)):
                nan_pts = np.where(np.isnan(dat))[0]
                dat[nan_pts] = datraw[nan_pts]

        setattr(group, aname, dat)
        if sumname not in labels:
            labels.append(sumname)
            sums[sumname] = dat
            if rawname != sumname:
                sums[rawname] = datraw
                if rawname not in labels:
                    labels.append(rawname)

        else:
            sums[sumname] = sums[sumname] + dat
            if rawname != sumname:
                sums[rawname] = sums[rawname] + datraw

    for name, dat in sums.items():
        if not hasattr(group, name):
            setattr(group, name, dat)

    for arrname in xdi.array_labels:
        sname = arrname.lower()
        if sname not in labels:
            labels.append(sname)

    for imca in range(nmca):
        setattr(group, 'ocr_mca%i' % (imca+1), ocrs[imca])
        setattr(group, 'icr_mca%i' % (imca+1), icrs[imca])


    group.array_labels = labels
    return group


DTC_header = '''# XDI/1.0  GSE/1.0
# Beamline.name:  13-ID-E, GSECARS
# Monochromator.name:  %(mono_cut)s, LN2 Cooled
# Monochromator.dspacing:  %(mono_dspace)s
# Facility.name: APS
# Facility.xray_source: 3.6 cm undulator
# Detectors.i0:  20cm ion chamber, He
# Detectors.ifluor:  Si SDD Vortex ME-4, 4 elements
# Detectors.ifluor_electronics:  Quantum Xspress3 3.1.10'''

def is_GSEXDI(filename):
    """test if file is GSE XDI data file
    reads only the first line of file
    """
    line1 = open(filename, 'r').readline()
    return (line1.startswith('#XDI/1') and 'Epics StepScan File' in line1)

@ValidateLarchPlugin
def gsexdi_deadtime_correct(fname, channelname, subdir='DT_Corrected',
                            bad=None, _larch=None):
    """convert GSE XDI fluorescence XAFS scans to dead time corrected files"""
    if not is_GSEXDI(fname):
        print("'%s' is not a GSE XDI scan file\n" % fname)
        return

    out = Group()
    out.orig_filename = fname
    try:
        xdi = read_gsexdi(fname, bad=bad, _larch=_larch)
    except:
        print('Could not read XDI file ', fname)
        return

    for attr in ('energy', 'i0', 'i1', 'i2', 'tscaler',
                 'counttime',  'scan_start_time', 'scan_end_time'):
        if hasattr(xdi, attr):
            setattr(out, attr, getattr(xdi, attr))

    # some scans may not record separate counttime, but TSCALER
    # is clock ticks for a 50MHz clock
    if not hasattr(out, 'counttime'):
        out.counttime = xdi.tscaler * 2.e-8

    if hasattr(xdi, 'energy_readback'):
        out.energy = xdi.energy_readback


    arrname = None
    channelname = channelname.lower().replace(' ', '_')

    for arr in xdi.array_labels:
        if arr.lower().startswith(channelname):
            arrname = arr
            break
    if arrname is None:
        print('Cannot find Channel %s in file %s '% (channelname, fname))
        return

    out.ifluor = getattr(xdi, arrname)
    out.ifluor_raw  = getattr(xdi, arrname)
    arrname_raw = arrname + '_nodtc'
    if arrname_raw  in xdi.array_labels:
        out.ifluor_raw  = getattr(xdi, arrname_raw)

    out.mufluor = out.ifluor / out.i0
    if hasattr(out, 'i1') or hasattr(out, 'itrans'):
        i1 = getattr(out, 'i1', None)
        if i1 is None:
            i1 = getattr(out, 'itrans', None)
        if i1 is not None:
            i1 = i1 / out.i0
            i1[np.where(i1<2.0e-20)] = 2.0e-20
            out.mutrans = -np.log(i1)

    npts   = len(out.energy)
    buff =  ['# XDI/1.0  GSE/1.0']

    header = OrderedDict()

    hgroups = ['beamline', 'facility', 'mono', 'undulator', 'detectors',
               'scaler', 'detectorstage', 'samplestage', 'scan', 'scanparameters']
    hskip = ['scanparameters.end', 'scanparameters.start']
    for agroup in hgroups:
        attrs = xdi._xdi.attrs.get(agroup, {})
        if agroup == 'mono': agroup = 'monochromator'
        header[agroup] = OrderedDict()
        for sname in sorted(attrs.keys()):
            if "%s.%s" %( agroup, sname) not in hskip:
                header[agroup][sname] = attrs[sname]


    header['facility']['name'] = 'APS'
    header['facility']['xray_source'] = '3.6 cm undulator'
    header['beamline']['name'] = '13-ID-E, GSECARS'

    header['detectors']['i0'] = '20cm ion chamber, He'
    header['detectors']['ifluor'] = 'Si SDD Vortex ME-4, 4 elements'
    header['detectors']['ifluor_electronics'] = 'Quantum Xspress3 3.1.10'

    mono_cut = 'Si(111)'
    if xdi.mono_dspacing < 2:
        mono_cut = 'Si(311)'
    header['monochromator']['name'] = "%s, LN2 cooled"  % mono_cut

    out_arrays = OrderedDict()
    out_arrays['energy']  = ('energy', 'eV')
    out_arrays['mufluor'] = ('mufluor', None)
    if hasattr(out, 'i1'):
        out_arrays['mutrans'] = ('mutrans', None)

    out_arrays['ifluor']  = ('ifluor', '# deadtime-corrected')
    out_arrays['ifluor_raw'] = ('ifluor_raw', '# not deadtime-corrected')
    out_arrays['i0'] = ('i0', None)

    if hasattr(out, 'i1'):
        out_arrays['itrans'] = ('i1', None)
    if hasattr(out, 'i2'):
        out_arrays['irefer'] = ('i2', None)

    if hasattr(out, 'counttime'):
        out_arrays['counttime'] = ('counttime', 'sec')

    arrlabel = []
    for iarr, aname in enumerate(out_arrays):
        lab = "%12s " % aname
        if iarr == 0: lab = "%11s " % aname
        arrlabel.append(lab)
        extra = out_arrays[aname][1]
        if extra is None: extra = ''
        buff.append("# Column.%i: %s %s" % (iarr+1, aname, extra))

    arrlabel = '#%s' % (' '.join(arrlabel))
    ncol = len(out_arrays)

    for family, fval in header.items():
        for attr, val in fval.items():
            buff.append("# %s.%s: %s" % (family.title(), attr, val))


    buff.append("# ///")
    for comment in xdi._xdi.comments.split('\n'):
        c = comment.strip()
        if len(c) > 0:
            buff.append('# %s' % c)
    buff.extend(["# summed %s fluorescence data from %s" % (channelname, fname),
                 "# Dead-time correction applied",
                 "#"+ "-"*78,   arrlabel])

    efmt = "%11.4f"
    ffmt = "%13.7f"
    gfmt = "%13.7g"
    for i in range(npts):
        dline = ["", efmt % out.energy[i], ffmt % out.mufluor[i]]

        if hasattr(out, 'i1'):
            dline.append(ffmt % out.mutrans[i])

        dline.extend([gfmt % out.ifluor[i],
                      gfmt % out.ifluor_raw[i],
                      gfmt % out.i0[i]])

        if hasattr(out, 'i1'):
            dline.append(gfmt % out.i1[i])
        if hasattr(out, 'i2'):
            dline.append(gfmt % out.i2[i])
        if hasattr(out, 'counttime'):
            dline.append(gfmt % out.counttime[i])

        buff.append(" ".join(dline))
    ofile = fname[:]
    if ofile.startswith('..'):
        ofile = ofile[3:]
    ofile = ofile.replace('.', '_') + '.dat'
    ofile = os.path.join(subdir, ofile)
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    try:
       fout = open(ofile, 'w')
       fout.write("\n".join(buff))
       fout.close()
       print("wrote %s, npts=%i, channel='%s'" % (ofile, npts, channelname))
    except:
       print("could not open / write to output file %s" % ofile)

    return out

def registerLarchPlugin():
    return ('_io', {'read_gsexdi': read_gsexdi,
                    'gsexdi_deadtime_correct': gsexdi_deadtime_correct})
