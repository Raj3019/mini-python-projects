import pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard

"""
Example:- 

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.say("The quick brown fox jumped over the lazy dog.")
engine.runAndWait()

"""

pdf = None
stop_thread = False                         # Variable signal stopping the playback

def play(pdfReader):
    global pdf
    global stop_thread

    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')                  # change voices
    rate = speaker.getProperty('rate')                      # change rate of speed
    volume = speaker.getProperty('volume')                  # Increase or Decrease the volumne

    for page_num in range(len(pdfReader.pages)):
        if stop_thread:
            break                                           # Exit the loop,if stop_thread is true
        text = pdfReader.pages[page_num].extract_text()
        speaker.setProperty('rate',rate-10)                 # Change the rate of speed. (+) for fast and (-) for slow
        # speaker.setProperty('voice', voices[0].id)        # changing index, changes voices. 0 for male
        speaker.setProperty('voice', voices[1].id)          # changing index, changes voices. 1 for female
        speaker.setProperty('volume', 0.50)                 # Setting up volume level  between 0 and 1
        # speaker.save_to_file(text,'sample.mp3')           # Save Voice to File 
        speaker.say(text)                                   
        speaker.runAndWait() 

    speaker.stop()

def stop_playback():
    global stop_thread
    input("Press Enter to stop playback....")
    stop_thread = True       # set the flag to stop playback

file = input("Enter your Pdf File name: ")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print('An error occurred:\n',e)
        print('\nEnter the file name again:\n')
        file = input("Enter your file name: ")

# create a seprate thread for the playblack
playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

#Start a thread for stopping playblack with keyboard input 
keyboard.add_hotkey("q",lambda:stop_playback())
keyboard.wait()  # wait for the hot key event

# wait for playback to finish
playback_thread.join()
