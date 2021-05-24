from pygame import mixer

mixer.init()
    
mixer.music.load("song.mp3")

mixer.music.set_volume(0.7)

mixer.music.play()

while True:
    print("Press p to pause and r to resume")
    print("press e to exit the program")
    query = input("Enter query: ")
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
        
    
    
