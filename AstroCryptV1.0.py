import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import Tkinter
from Tkinter import *
import tkFileDialog
import tkMessageBox
filename = None
password = None


def encrypt(key , filename):
    chunksize = 64 * 1024
    outputFile = filename+".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''

    for i in range(16):
        IV += chr(random.randint(0, 0xFF))

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename[:-4]

    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)


def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

def load_file():
    global password, filename
    text_file = tkFileDialog.askopenfile()
    if text_file.name != None:
        filename = text_file.name
        var.set(filename)


def encrypt_the_file():
    global filename, password
    if filename != None:
        password = passInput.get()
        encrypt(getKey(password), filename)
        # sys.stdout.write('Password is ' + password)
        # encrypt_file(filename, password)
    else:
        tkMessageBox.showerror(title="Error", message="There was no file loaded to encrypt")


def decrypt_the_file():
    global filename, key
    if filename != None:
        password = passInput.get()
        decrypt(getKey(password), filename)
        # sys.stdout.write('gonna decrypt the file' + '\n')
        # decrypt_file(fname, password)
    else:
        tkMessageBox.showerror(title="Error", message="There was no file loaded to decrypt")

def donothing():
   filewin = Toplevel(root)
   mystring = StringVar()
   mystring= '''AstroCrypt is an encryption - decryption tool written in Python which uses AES-CBC encryption technique. It uses the AES-256-CBC cipher and encodes the encrypted
    data with Base64. In simple terms, user can use the tool to encrypt their files whatsoever it may be,
     for example a text file , an image, an audio-video file , a pdf , or a typical openXML with a password
     and can keep them safe until it is decrypted using the same password.'''

   labelU = Label(filewin, text=mystring)
   labelU.configure(wraplength=300, bg='turquoise', fg='Black',activebackground='coral')
   labelU.pack()

root = Tkinter.Tk()
root.title("AstroCrypt v 1.0 ")
root.geometry("300x250")
root.configure(background='turquoise')

menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0, activebackground='coral', bg='turquoise')

helpmenu.add_command(label="About AstroCrypt", command=donothing)
helpmenu.add_command(label="Quit the tool", command=root.quit)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


# GUI STUFF over here
# l = Label(root, text="AstroCrypt")
# l.configure(background='beige')
# l.pack(side=TOP, padx=0, pady=20, fill=X)

frame = Frame(root)
frame.pack(padx=0, pady=30)
frame.configure(background='turquoise')

var = StringVar()
Filelabel = Label(frame, textvariable=var, relief=FLAT)
Filelabel.configure(bg='white', fg='Black', anchor=E, font=("default", 8), padx=4, pady=4, activebackground='coral', width=50)
var.set(" Check the path here !!!")
Filelabel.pack(side=TOP, padx=10, pady=0)

loadButton = Tkinter.Button(frame, text="   LOAD FILE   ", command=load_file)
loadButton.pack(side=RIGHT, padx=10, pady=5, fill=X)
loadButton.configure(bg='turquoise4', fg='white', activebackground='coral')

frame1 = Frame(root)
frame1.pack(padx=0, pady=0)
frame1.configure(background='turquoise')
frame2 = Frame(root)
frame2.pack(padx=0, pady=40)
frame2.configure(background='turquoise')

l1 = Label(frame1, text="ENTER KEY")
l1.configure(background='turquoise')
passInput = Entry(frame1, show="*", width=30)
password = passInput.get()
encryptButton = Tkinter.Button(frame2, text="       ENCRYPT      ", command=encrypt_the_file)
encryptButton.configure(bg='turquoise4', fg='white', activebackground='coral')
decryptButton = Tkinter.Button(frame2, text="       DECRYPT      ", command=decrypt_the_file)
decryptButton.configure(bg='turquoise4', fg='white', activebackground='coral')

l1.pack(side=LEFT, padx=5, pady=0, fill=X)
passInput.pack(side=RIGHT, padx=5, pady=0, fill=X)
encryptButton.pack(side=LEFT, padx=10, pady=0, fill=X)
decryptButton.pack(side=RIGHT, padx=10, pady=0, fill=X)
root.mainloop()
