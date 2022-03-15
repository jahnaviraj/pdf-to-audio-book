"""Handle requests return audio output"""

from gtts import gTTS

class AudioBook():
    """Convert text into speech and saved it in mp3 file."""

    def __init__(self) -> None:
        pass

    def generate_audio(self, text):
        text = text.replace("\n", " ")
        audio_obj = gTTS(text=text, lang="en", slow=False)
        audio_obj.save("audio-book.mp3")

