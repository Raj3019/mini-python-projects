import pyttsx3
import keyboard
import threading

speaker = pyttsx3.init()

def text_to_speech():
    speaker.say("For years, Facebook gave some of the world's largest technology companies more intrusive access to users' personal data than it has disclosed, effectively exempting those business partners from its usual privacy rules, according to internal records and interviews The special arrangements are detailed in hundreds of pages of Facebook documents obtained by The New York Times The records, generated in 2017 by the company's internal system for tracking partnerships, provide the most complete picture yet of the social network's data-sharing practices They also underscore how personal data has become the most prized commodity of the digital age, traded on a vast scale by some of the most powerful companies in Silicon Valley and beyond The exchange was intended to benefit everyone Pushing for explosive growth, Facebook got more users, lifting its advertising revenue Partner companies acquired features to make their products more attractive Facebook users connected with friends across different devices and websites But Facebook also assumed extraordinary")
    speaker.runAndWait()

def stop_on_key_press():
    while True:
        if keyboard.is_pressed('q'):
            print("Stopping speech...")
            # Stop the speech engine
            speaker.stop()
            break

# Start the text-to-speech process in a separate thread
speech_thread = threading.Thread(target=text_to_speech)
speech_thread.start()

# Start a separate thread to check for key press
key_press_thread = threading.Thread(target=stop_on_key_press)
key_press_thread.start()

# Wait for the text-to-speech thread to finish
speech_thread.join()
