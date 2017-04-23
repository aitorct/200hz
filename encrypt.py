from __future__ import print_function, division, unicode_literals
import wave
import functions as fnc
import numpy as np
# compatibility with Python 3

def encryptMessage( path ):

    fileName = '200hz_.wav'

    # Created input file if not exists with:
    wr = wave.open(path, 'r')
    par = list(wr.getparams())
    par[3] = 0

    #output file
    ww = wave.open(fileName, 'w')
    ww.setparams(tuple(par))

    lowpass = 200
    #highpass = 1000

    sz = wr.getframerate()
    c = int(wr.getnframes()/sz)
    #user input
    #message = input("Write the secret message: ")
    message = "00000000123456789abcdefghijklmnopqrstuvwxyz"
    print("Message Accepted")

    # print('Processing {}/{} s'.format(num+1, c))
    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    # left and right channel
    left, right = da[0::2], da[1::2]
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    lf[:lowpass], rf[:lowpass] = 0, 0
    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)

    # nl[:lowpass], nr[:lowpass] = 0, 0 # Lowpast Postcalculations

    lenght = len(message)

    nl[0], nr[0] = lenght, lenght

    if len(message) < lowpass:
        k = 1
        for char in message:

            temp = fnc.encryptChar(char)
            #nl[k], nr[k] = temp, temp
            # print("Value"+str(temp))
            lf[k], rf[k] = temp, temp

            k = k + 1
    #print( "lf encrypt")
    #for u in lf:
    #    print( str(u) )

    ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
    ns2 = ns * 2
    ww.writeframes(ns2.tostring())


    wr.close()
    ww.close()
