from win32com.client import Dispatch

def speak(text):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(text)


if __name__ == "__main__":
    while True:
        query = str(input('Enter what to speak:\n'))

        speak(query)