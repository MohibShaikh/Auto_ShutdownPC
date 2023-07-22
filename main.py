import speech_recognition as sr
import subprocess


def shutdown_laptop():
    subprocess.call(["shutdown", "-s", "-t", "0"])


def listen_for_phrase():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for phrase...")
        audio = r.listen(source)

    try:
        phrase = r.recognize_google(audio).upper()
        print("Recognized phrase:", phrase)
        if phrase == "SHUTDOWN DARLING":
            print("Shutting down...")
            shutdown_laptop()
        else:
            print("Phrase does not match.")
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))


listen_for_phrase()
