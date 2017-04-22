from __future__ import print_function, division, unicode_literals
import wave
import functions as fnc
import numpy as np
import matplotlib.pyplot as plt
# compatibility with Python 3

# Created input file if not exists with:
wr = wave.open('input.wav', 'r')
par = list(wr.getparams()) 
par[3] = 0

#output file
ww = wave.open('filtered-output.wav', 'w')
ww.setparams(tuple(par))

lowpass = 200 
#highpass = 1000 

sz = wr.getframerate()
#whole file
c = int(wr.getnframes()/sz)
#user input
message = raw_input("Write the secret message: ")

for num in range(c):
    print('Processing {}/{} s'.format(num+1, c))
    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    # left and right channel
    left, right = da[0::2], da[1::2] 
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    lf[:lowpass], rf[:lowpass] = 0, 0

    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
    ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
    ww.writeframes(ns.tostring())

# for num in lf:
#     print(int(num))

wr.close()
ww.close()