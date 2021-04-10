#modules
import speech_recognition as sr

# step 1: listen
listener = sr.Recognizer()
try:
    with sr.Microphone() as source :
        print('speak : ')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    print('probleme:\n -microphone non reconue.\n -module python incompatible avec Pyaudio \n - autres ... ')
