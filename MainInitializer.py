from Image.helper import AdvanceImageDisplay
from Image.utils import openFile
from tkinter import *
from Image.functions import encryption,key

def call_Decryptor():
    path=openFile.open_file()
    if path != None:
        win1 = Toplevel(root)
        AdvanceImageDisplay.Zoom_Advanced(win1,path=path)
    return

def call_Encryptor():
    path=openFile.open_file()
    if path != None:
        encryption.encrypt(path, key.load_key())
    return


# the first gui owns the root window
if __name__ == "__main__":
    root = Tk()
    root.title('Fresco')
    root.geometry("200x200")
    root.iconbitmap('D:\DigitalWorkHome\eclipseworkspace\pythonworkspace\CrytoImageLoader\Image\images\delta.ico') 
    button_1 = Button(root, text='Decrypt Image', command=call_Decryptor)
    button_1.pack()
    button_2 = Button(root, text='Encrypt Image',command=call_Encryptor)
    button_2.pack()
    root.mainloop()