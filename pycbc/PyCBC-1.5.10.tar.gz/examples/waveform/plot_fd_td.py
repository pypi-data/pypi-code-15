# Plot a time domain and fourier domain waveform together in the time domain.
# Note that without special cleanup the Fourier domain waveform will exhibit
# the Gibb's phenomenon. (http://en.wikipedia.org/wiki/Gibbs_phenomenon)

import pylab
from pycbc import types, fft, waveform

# Get a time domain waveform
hp, hc = waveform.get_td_waveform(approximant="EOBNRv2",
                             mass1=6, mass2=6, delta_t=1.0/4096, f_lower=40)
                             
# Get a frequency domain waveform
sptilde, sctilde = waveform. get_fd_waveform(approximant="TaylorF2",
                             mass1=6, mass2=6, delta_f=1.0/4, f_lower=40)

# FFT it to the time-domain  
tlen = 1.0 / hp.delta_t / sptilde.delta_f
sptilde.resize(tlen/2 + 1)
sp = types.TimeSeries(types.zeros(tlen), delta_t=hp.delta_t)                            
fft.ifft(sptilde, sp)

pylab.plot(sp.sample_times, sp, label="TaylorF2 (IFFT)")
pylab.plot(hp.sample_times, hp, label="EOBNRv2")

pylab.ylabel('Strain')
pylab.xlabel('Time (s)')
pylab.legend()
pylab.show()
