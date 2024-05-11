import mysql.connector
from tkinter import *
from tkinter import messagebox
import sounddevice
from scipy.io.wavfile import write
import soundfile
from tkinter import filedialog
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import speech_recognition as sr
class AdminHome:
    def __init__(self,master):
        self.master=master
        self.duration=StringVar()
        self.fpath=StringVar()
        self.lbl_text=StringVar()

        self.lbl_text.set("waiting")
        #master1 = Toplevel()
        master.title("Admin Home")
        master.state("zoomed")
        large_font = ('Verdana', 25)

        lbl_2 = Label(master, text="Duration", height=2, width=20, font=large_font).place(x=700, y=10)
        dur = Entry(master,textvariable=self.duration, width=3, font=large_font).place(x=1000, y=20)
        #dur = Entry(master, text="Select a Voice...", width=20, font=large_font).place(x=400, y=20)
        sbmitbtn = Button(master, text="RECORD VOICE", height = 2, width = 20,font=large_font,command=self.recordvoice ).place(x=700, y=75)
        lbl = Label(master, text="Select a Voice...", height=2, width=20, font=large_font).place(x=700, y=200)
        voice_emotion = Label(master,textvariable=self.lbl_text, text="Emotion...", height=2, width=20, font=large_font).place(x=100, y=200)
        txt = Entry(master,textvariable=self.fpath, width=20, font=large_font).place(x=700, y=300)
        browse = Button(master, text="Browse",  font=large_font,command=self.browsefunc).place(x=1150, y=300)
        emotion = Button(master, text="VIEW EMOTION", height=2, width=20, font=large_font,command=self.viewemotion).place(x=700, y=400)
        ext = Button(master, text="Exit", height=2, width=20, font=large_font,command=master.destroy).place(x=700, y=550)
        master.mainloop()

    def browsefunc(self):
        print("browse here")

    def viewemotion(self):
        print("started...")

    def recordvoice(self):
        print("record")
cp=Tk()
w=AdminHome(cp)
