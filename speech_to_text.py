import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Recognizing...")
    audio_data = r.record(source, duration=5)
    # convert speech to text
    text: str = r.recognize_google(audio_data, language="pt-BR")
    print(text)
    f = open("texto_transcrito.txt", "w")
    f.write(text)
