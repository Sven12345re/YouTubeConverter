import tkinter as tk
from urllib.request import urlopen

from pytube import YouTube
from PIL import Image, ImageTk

videoInfos = []


def downloadvid():
    string = E1.get()
    yt = YouTube(str(string))
    stream = yt.streams.first()
    stream.download("Downloads")


def loaddetail():
    global E1
    global exceptlabel
    string = E1.get()
    global label
    global titleVideo
    global button

    try:
        if titleVideo != '':
            print("Test")
            label.pack_forget()
            titleVideo.pack_forget()
            button.pack_forget()

        yt = YouTube(str(string))
        image = Image.open(urlopen(yt.thumbnail_url))
        image.thumbnail((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image=photo)
        label.image = photo
        label.pack()
        titleVideo = tk.Label(root, text=yt.title)
        titleVideo.pack()
        button = tk.Button(root, text="Download", fg="red", command=downloadvid)
        button.pack()
        exceptlabel.pack_forget()
    except:
        if exceptlabel.cget("text") == '':
            exceptlabel = tk.Label(root, text='Ungültige URL')
            exceptlabel.pack()


root = tk.Tk()




w = tk.Label(root, text="Youtube Downloader")
w.pack()

name = tk.StringVar()
E1 = tk.Entry(root, bd=5, textvariable=name)
name.trace("w", lambda l, idx, mode: loaddetail())
E1.pack(fill='x')
exceptlabel = tk.Label(root, text='')
titleVideo = ''

root.mainloop()
