import speech_recognization as sr
audio_file = ("audio.wav")

r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    print("Audio file contains: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Could not get results from Google Speech Recognition")