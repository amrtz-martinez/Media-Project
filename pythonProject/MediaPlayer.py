"""
Build An MP3 Player With Tkinter
By: John Elder
Youtube: https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw
Website: Codemy.com
"""

from tkinter import *
import pygame
from PIL import Image, ImageTk
from tkinter import filedialog


root = Tk()
root.title('Gestural Media Player')
root.geometry("500x550")
#root.configure(background="white")

#Intialize Pygame Mixer for audio
pygame.mixer.init()

label = Label(root, text="Gestural Media Player", fg="black", font="arial 25")
label.pack()

########################################################################################################################
# 1 finger to play the current song
clickLabel = Label(root, text="1 finger to play the first song added", fg="black", font="arial 20", pady=10)
# 2 fingers plays the next song
clickLabel_2 = Label(root, text="2 fingers to play the next song", fg="black", font="arial 20", pady=10)
# 3 fingers play the previous song
clickLabel_3 = Label(root, text="3 fingers to play the previous song", fg="black", font="arial 20", pady=10)
# 5 fingers stops the song
clickLabel_5 = Label(root, text="5 fingers to stop the song", fg="black", font="arial 20", pady=10)


# Hide and show label
def hide(x):
    #This will remove the widget
    #clickLabel.pack_forget()
    #clickLabel_2.pack_forget()
    #clickLabel_3.pack_forget()
    #clickLabel_5.pack_forget()

    x.pack_forget()

    #clickLabel.pack()
    #clickLabel_2.pack()
    #clickLabel_3.pack()
    #clickLabel_5.pack()


# Show the label
def show(x):
    clickLabel.pack()
    clickLabel_2.pack()
    clickLabel_3.pack()
    clickLabel_5.pack()

    x.pack_forget()

    #clickLabel.pack_forget()
    #clickLabel_2.pack_forget()
    #clickLabel_3.pack_forget()
    #clickLabel_5.pack_forget()

########################################################################################################################


button = Button(root, text="Click here for Directions for Controls", fg="black", font="arial 15", pady=10, command=show)
#button2 = Button(MusicPlayer, text="Close", fg="red", font="arial 15", pady=10, command=hide)
#button.configure(command=lambda: show())
button.configure(command=lambda: show(button))

button.pack()
#button2.pack()

#Add Song Function
def addSong():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    #Replaces direectory info with name of song (Will need to edit yourselves when testing to fit your own device)
    song = song.replace("/Users/manuel/Desktop/pythonProject/audio/", "")
    song = song.replace(".mp3", "")

    song_box.insert(END, song)
    song_box.select_set(0)

#Add multiple songs
def addMultipleSongs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    #Loops through songs and replace directory info
    for song in songs:
        song = song.replace("/Users/manuel/Desktop/pythonProject/audio/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)
        song_box.select_set(0)

#Delete a song
def deleteSong():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

#Delete all songs
def deleteAllSongs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()

#Play selected song
def play():
    song = song_box.get(ACTIVE)
    #Change this line to fit your directory again
    song = f'/Users/manuel/Desktop/pythonProject/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

#Create global pause variable
global paused
paused = False

#Pause and unpause current song
def pause(isPaused):
    global paused
    paused = isPaused

    if paused:
        # unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # pause
        pygame.mixer.music.pause()
        paused = True

#Play next song
def nextSong():
    #Get current song tuple number
    nextOne = song_box.curselection()
    #Add one to current song number
    nextOne = nextOne[0]+1
    #Grab song title from playlist
    song = song_box.get(nextOne)

    song = f'/Users/manuel/Desktop/pythonProject/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Clear active song bar
    song_box.selection_clear(0, END)
    #Select new song
    song_box.activate(nextOne)
    song_box.selection_set(nextOne, last=None)

#Play previous song in playlist
def previousSong():
    # Get current song tuple number
    nextOne = song_box.curselection()
    # Subtract one to current song number
    nextOne = nextOne[0] - 1
    # Grab song title from playlist
    song = song_box.get(nextOne)

    song = f'/Users/manuel/Desktop/pythonProject/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active song bar
    song_box.selection_clear(0, END)
    # Select new song
    song_box.activate(nextOne)
    song_box.selection_set(nextOne, last=None)


#Create Playlist Box
song_box = Listbox(root, bg="lightblue", fg="black", width=60, selectbackground="grey", selectforeground="white")

song_box.pack(pady=20)

#Create Media Player Buttons Images
backImg = ImageTk.PhotoImage(Image.open('images/back.png'))
pauseImg = ImageTk.PhotoImage(Image.open('images/pause.png'))
playImg = ImageTk.PhotoImage(Image.open('images/play.png'))
#stopImg = ImageTk.PhotoImage(Image.open('images/stop.png'))
nextImg = ImageTk.PhotoImage(Image.open('images/next.png'))

#Create Media Player Frame
controls_frame = Frame(root)
controls_frame.pack()

#Create Media Player Buttons
backButton = Button(controls_frame, image=backImg, width=0, command=previousSong)
pauseButton = Button(controls_frame, image=pauseImg, width=0, command=lambda: pause(paused))
playButton = Button(controls_frame, image=playImg, width=0, command=play)
#stopButton = Button(controls_frame, image=stopImg, width=0, command=stop)
nextButton = Button(controls_frame, image=nextImg, width=0, command=nextSong)


backButton.grid(row=0, column=0, padx=10)
pauseButton.grid(row=0, column=1, padx=10)
playButton.grid(row=0, column=2, padx=10)
#stopButton.grid(row=0, column=3, padx=10)
nextButton.grid(row=0, column=4, padx=10)

#Create Menu
myMenu = Menu(root)
root.config(menu=myMenu)

#Add Song Menu
addSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Add Songs", menu=addSongMenu)
addSongMenu.add_command(label="Add Song to Playlist", command=addSong)
#Add Multiple Songs
addSongMenu.add_command(label="Add Mutiple Songs to Playlist", command=addMultipleSongs)

#Create Delete Song Menu
removeSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Remove Songs", menu=removeSongMenu)
removeSongMenu.add_command(label="Delete a song", command=deleteSong)
removeSongMenu.add_command(label="Delete all songs", command=deleteAllSongs)

#creating the help menu
helpMenu = Menu(myMenu)
myMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Controls")

root.mainloop()

#insert one script into another and use threads to work together
#run both files together and use pip to send data







