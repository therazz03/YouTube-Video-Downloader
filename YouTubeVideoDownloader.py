#!/usr/bin/env python3


from tkinter import *
from pytube import YouTube

def youtube():
	yt = YouTube(link.get())
	yt.title  # to get the title of the video
	stream = yt.streams.first()
	stream.download('/Downloads/') # address where the file will be downloaded 
	print("Download Complete")

root = Tk()
root.title("YouTube Video Downloader")
root.geometry('350x200')
thelabel = Label(root, text='Enter link to download video')
thelabel.pack()
link = Entry(root)
link.pack()
button = Button(root, text='Download', command = youtube)
button.pack()
root.mainloop()
