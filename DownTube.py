from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image


def accion():
    if r.get() == 1:
        enlace = videos.get()
        video = YouTube(enlace)
        descarga = video.streams.get_audio_only()
        descarga.download()
        videos.delete(0, END)
        MessageBox.showinfo('Terminado', 'Descarga finalizada!')
    else:
        enlace = videos.get()
        video = YouTube(enlace)
        descarga = video.streams.get_highest_resolution()
        descarga.download()
        videos.delete(0, END)
        MessageBox.showinfo('Terminado', 'Descarga finalizada!')

def popup():
    MessageBox.showinfo("Sobre mí", "Enlace a mi portafolio")

root = Tk()
root.config(bd=15)
root.title("Descarga videos de YouTube")
root.geometry('400x200')

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para mas información", menu=helpmenu)
helpmenu.add_command(label="Información del Autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="\tPega en la casilla el enlace completo que desea obtener\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

r = IntVar()
r.set('1')

audio = Radiobutton(root, text='Audio', variable=r, value=1)
audio.grid(row=2, column=1)
audiovideo = Radiobutton(root, text='Video', variable=r, value=2)
audiovideo.grid(row=3, column=1)

boton = Button(root, text="Descargar :)", command=accion)
boton.grid(row=4, column=1)


videos.focus()
mainloop()