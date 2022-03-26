from tkinter import *
from pytube import YouTube




def save_video():
    YouTube("https://youtu.be/0IAr0HhOVZo").streams.first().download(path.get())
    secwin = Tk()
    downloaded = Label(secwin, text = "Successfully Downloaded Video!")
    downloaded.pack()
    
    

mainwin = Tk()
mainwin.geometry("950x700")


welcome = Label(mainwin, text = "YOUTUBE VIDEO DOWNLOADER BY KUSH")
welcome.grid(row = 0, column =0)

enter_link = Label(mainwin, text = "Enter Link Here - ")
enter_link.grid(row = 2, column = 0, pady = 50)

link = Entry(mainwin, borderwidth = 8, width =25)
link.place(x = 100, y = 170)

enter_path = Label(mainwin, text = "Please Enter The File Path to Save the Video")
enter_path.place(x = 20, y = 300)

path = Entry(mainwin, borderwidth = 8, width = 25)
path.place(x = 100, y = 360)



download_button = Button(mainwin, text = "DOWNLOAD", bg = "red", command = save_video)
download_button.place(x = 240, y = 550)






mainwin.mainloop()

#Important Variables
yt_link = str(link.get())
filepath = str(path.get())







