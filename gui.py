from tkinter import *
#from decr
#from decrypt import decryptMessage
import tkinter.filedialog, tkinter.ttk, time, random, encrypt, decrypt



root = Tk()
root.wm_title("")
root.configure(bg='#ececec')

topFrame = Frame(root)
topFrame.configure(bg='black')
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

title_opt = {'padx': 50, 'pady': 30}
button1_opt = {'padx': 15, 'pady': 30}
button2_opt = {'padx': 15}
pb_opt = {'padx': 10, 'pady': 50}
of_opt = {}
of_opt['filetypes'] = [('WAV files','.wav')]


def openFile():
    filename = tkinter.filedialog.askopenfilename(**of_opt)

    if filename:
        barProgress()
        return filename

    #if filename:
    #    return open(filename, 'r')


def barProgress():
    global mpb
    progress = 0
    while progress < 100:
        progress += random.randint(0,20)
        mpb['value'] = progress
        mpb.update()
        time.sleep(random.uniform(0,0.5))


def callback_b1():
    name = openFile()
    print("[Encrypt] " + name)
    encrypt.encryptMessage(name)


def callback_b2():
    name = openFile()
    print("[Decrypt] " + name)
    decrypt.decryptMessage(name)


title = Label(topFrame, text="200Hz", font=("Helvetica", 48), fg="white", background='black')
title.pack(title_opt)

openButton = Button(root, text='Encrypt file', background="#ececec", highlightbackground='#ececec', command=callback_b1)
openButton.pack(button1_opt)

saveButton = Button(root, text='Decrypt file', background = "#ececec", highlightbackground='#ececec', command=callback_b2)
saveButton.pack(button2_opt)

mpb = tkinter.ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", value=0, maximum=100)
mpb.pack(pb_opt)


root.mainloop()
