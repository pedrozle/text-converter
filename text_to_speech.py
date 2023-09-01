from gtts import gTTS
from pathlib import Path

text = ""
with open("texto_transcrito.txt", encoding="utf-8") as f:
    for s in f:
        text += str(s)
    text = text.replace("\n", "")
    print(text)

    audio = gTTS(text, slow=False, lang="pt")
    audio.save("audio.mp3")
