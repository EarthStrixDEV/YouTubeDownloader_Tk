from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import threading

app = Tk()
app.title("YouTube Download")
app.resizable(width=False, height=False)

def handle_selection(selection):
    global selectFormat
    selectFormat = 1 if selection == "Audio" else 2

def downloader():
    link = url_text.get()
    if len(link) == 0:
        messagebox.showerror('Alert','Please push your url :(')
        return
    if link.startswith('https://youtu'):
        messagebox.showerror('Alert','Please push only youtube url :(')
        return
    try:
        video = YouTube(link)
        if selectFormat == 1:
            stream = video.streams.get_audio_only()
        elif selectFormat == 2:
            stream = video.streams.get_highest_resolution()
        stream.download()
    except:
        messagebox.showerror('Alert','Could not download video :(')
    else:
        messagebox.showinfo('Alert','Download video successfully :)')

selected_option = StringVar()
url_text = StringVar()

Label(app ,text="YouTube Downloader",font=("Prompt",12)).grid(row=0 ,column=1 ,sticky=W ,padx=30 ,pady=10)
Label(app ,text="Url",font=("Prompt",9)).grid(row=1 ,column=0 ,sticky=W ,padx=8 ,pady=10)
Entry(app ,textvariable=url_text ,font=('Arial',12)).grid(row=1 ,column=1 ,padx=0 ,pady=5)
Label(app ,text="Format",font=("Prompt",9)).grid(row=1 ,column=2 ,padx=8 ,pady=10)
OptionMenu(app ,selected_option ,"Audio" ,"Video" ,command=handle_selection).grid(row=1 ,column=3 ,padx=0 ,pady=3)
Button(app ,text='Download' ,font=('Prompt',9) ,command=lambda: threading.Thread(target=downloader).start()).grid(row=1 ,column=4 ,padx=5 ,pady=5)

app.mainloop()