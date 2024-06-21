#pip install SpeechRecognition
#pip install pyaudio
import speech_recognition as sr

def listenVoiceAndSave(voiceFilePath):
    
    recognizer = sr.Recognizer()

    with sr.Microphone() as voiceSource:
        print("listening ~ /// . ///")
        voice = recognizer.listen(voiceSource)
        print("Recognize Down")

        with open(voiceFilePath, 'wb') as voiceFile: #write/Byte Mode
            voiceFile.write(voice.get_wav_data())
