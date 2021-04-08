from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/",title="Please select a file")
    current_song = filename
    song_title   = filename.split("/")
    song_title   = song_title[-1]
    
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green",text="Now playing : " + str(song_title))
        volume_label.config(fg="green",text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error playing track")
