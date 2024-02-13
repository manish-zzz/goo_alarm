import pyttsx3

class TextToSpeechBase():
    # Initialize the pyttsx3 engine with eSpeak
    engine = pyttsx3.init(driverName='espeak')

    def speak(self):
        self.engine.say("Hello, Hello")
        self.engine.runAndWait()

class TextToSpeech(TextToSpeechBase):
    def __init__(self) -> None:
        super().__init__()

        # Set properties (optional)
        self.engine.setProperty('rate', 130)  # Speed of speech

    def speak(self, text):
        super().speak()

        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    txt_spk = TextToSpeech()
    txt_spk.speak("")