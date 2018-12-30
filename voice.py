#!/usr/bin/env python3

import speech_recognition as sr
def voice_to_text():
# get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        voice = r.recognize_google(audio)
        print(voice)
        return voice
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


