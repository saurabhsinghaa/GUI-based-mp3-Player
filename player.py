from tkinter import *
import pygame
from tkinter import filedialog


def addSong():
    song = filedialog.askopenfilename(title="Choose A Song",filetypes=(("mp3 Files","*.mp3"), ))
    song = song.replace("C:/Users/HP/Music/","")
    song = song.replace(".mp3","")
    song_box.insert(END,song)
def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/HP/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
# global pause variable
global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True
def addManySong():
    songs = filedialog.askopenfilenames(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace("C:/Users/HP/Music/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)
def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    song = f'C:/Users/HP/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0,END)
    song_box.activate(next_one)
    song_box.selection_set(next_one,last=None)

def previous_song():
    next_one = song_box.curselection()
    next_one = next_one[0] - 1
    song = song_box.get(next_one)
    song = f'C:/Users/HP/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)



root = Tk()
root.title('MP3 PLAYER')
# root.iconbitmap('dsfdf')
root.geometry("470x285")
root.configure(bg='#f0d033')

pygame.mixer.init()   #pygame mixer
song_box = Listbox(root,bg="black",fg="green",width=60,selectbackground="gray",selectforeground="black") #playlist box
song_box.pack(pady=20)

backBtnImg = PhotoImage(file='prev.png')
forwardBtnImg = PhotoImage(file='next.png')
playBtnImg = PhotoImage(file='play.png')
pauseBtnImg = PhotoImage(file='pause.png')
stopBtnImg = PhotoImage(file='stop.png')

# Create control frame
controlFrame = Frame(root,bg='#f0d033')
controlFrame.pack()
# control button
backBtn = Button(controlFrame,image=backBtnImg,borderwidth=0,command=previous_song,bg='#f0d033')
forwardBtn = Button(controlFrame,image=forwardBtnImg,borderwidth=0,command=next_song,bg='#f0d033')
playBtn = Button(controlFrame,image=playBtnImg,borderwidth=0,command=play,bg='#f0d033')
pauseBtn = Button(controlFrame,image=pauseBtnImg,borderwidth=0,command=lambda: pause(paused),bg='#f0d033')
stopBtn = Button(controlFrame,image=stopBtnImg,borderwidth=0,command=stop,bg='#f0d033')

backBtn.grid(row=0,column=0,padx=10)
forwardBtn.grid(row=0,column=4,padx=10)
playBtn.grid(row=0,column=2,padx=10)
pauseBtn.grid(row=0,column=3,padx=10)
stopBtn.grid(row=0,column=1,padx=10)

# menu
myMenu = Menu(root)
root.configure(menu=myMenu)
# addSong menu
addSongMenu = Menu(myMenu,bg='#272725',fg='white')
myMenu.add_cascade(label='Add Song',menu=addSongMenu)
addSongMenu.add_command(label="Add One Song To Playlist",command=addSong)
addSongMenu.add_command(label="Add Many Songs To Playlist",command=addManySong)

root.mainloop()