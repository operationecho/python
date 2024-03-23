import time
import os, cursor
import pathlib, random
from inputimeout import inputimeout, TimeoutOccurred
from pygame import mixer



cursor.hide()

def main():
  print("""\n\n

Controls:
b\tbegin playback
n\tnext song
p\tpause song (not perfected yet)
r\tprevious song
s\tstop playback
u\tunpause song

  
""")

  importMusic()

  
  
def importMusic():
  print("something")
  musicPath = pathlib.Path("/media/Music/")
  musicPath.rglob("*")


  previouslyPlayed = {}
  playCount = 1
  musicList = []
  musicType = ["*.mp3","*.MP3", "*.flac", "*.FLAC", "*.wav", "*.WAV"]
  for type in musicType:
    for songFile in list(musicPath.rglob(type)):
      musicList.append(songFile)
    

  songCount = len(musicList)
  while songCount != 0:

    currentSong = musicList[random.randrange(0,songCount)]

    musicList.remove(currentSong)
    previouslyPlayed[playCount] = currentSong
    

    songCount = len(musicList)
    result = playMusic(currentSong)
    if result == "quit":
      quitApp()
      
    if result == 0:
      playCount += 1
      
    pendingPlayCount = playCount
    while result == 1:
      if playCount != 1:
        playCount -= 1
        previousSong = previouslyPlayed[playCount]
        result = playMusic(previousSong)
      else: 
        result = 0
        playCount += 1

    
  
  
    
  return (0)


def quitApp():
  exit()

def playMusic(currentSong):

  mixer.init()
  mixer.music.load(f"{currentSong}")
  mixer.music.play()
  x = 1
  while x == 1:
    while mixer.music.get_busy():  # wait for music to finish playing
      time.sleep(1)

        
      try:
        os.system('clear')
        print(f"Now Playing: {currentSong}")
        text = inputimeout(prompt=' ', timeout=1)
        if text.lower() == "p":
          mixer.music.pause()
          text = input("--song is paused--  ")
          if text.lower() == "u":
            mixer.music.unpause()
        if text.lower() == "s":
          mixer.music.stop()
          text = input("--song stopped-- ")
          if text.lower() == "b":
            mixer.music.play()
        if text.lower() == "n":
          x = 0
          return (0)
        if text.lower() == "r":
          x = 0
          return (1)
        if text.lower() == "q":
          mixer.music.stop()
          return("quit")

      except:
        continue

      finally:
        x = 1
         
    x = 0
    return(0)
          
          
if __name__ == '__main__':
  main()
  
