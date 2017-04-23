from __future__ import print_function, division, unicode_literals
import wave
import functions as fnc
import numpy as np


def decryptMessage( path ):

    wr = wave.open(path, 'r')
    par = list(wr.getparams())
    par[3] = 0


    lowpass = 200

    sz = wr.getframerate()
    c = int(wr.getnframes()/sz)


    # print('Processing {}/{} s'.format(num+1, c))
    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    left, right = da[0::2], da[1::2]
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)


    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)



    iterations = int(nl[0]) + 2
    # print("Iterations: "+str(iterations))
    finalMessage = []

    for j in range(1, iterations):
        #finalMessage.append( fnc.decryptValue( lf[j] ) )
        finalMessage.append( fnc.decryptValue( nl[j] ) );

    print(fnc.toString(finalMessage))


    wr.close()

    for i in nl:
        print("Value lf: "+str(int(i)))

    """
    print("*****************")

    for i in nr:
        print("Value nr: "+str(i))
    """
