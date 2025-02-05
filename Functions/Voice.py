import speech_recognition as sr
import pyttsx3
import pygame
import io
import random
from gtts import gTTS

# Initialize the text-to-speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()
def speak_text(text):
    print(text)
    # Convert the text to audio and save it to a memory buffer
    tts = gTTS(text=text, lang="fr")
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)  # Rewind the buffer

    # Initialize pygame mixer to play from the buffer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_buffer, "mp3")
    pygame.mixer.music.play()

    # Keep the program running until the audio finishes
    while pygame.mixer.music.get_busy():
        pass

def listen_for_keyword():
    """
    Continuously listens for the keyword 'assistant' in French.
    """
    print("Dites 'assistant' pour commencer à enregistrer votre question.")
    
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce noise sensitivity
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)  # Listen with timeout
                transcription = recognizer.recognize_google(audio, language="fr-FR")
                print(transcription)
                if transcription.lower() == "assistant":
                    print("Mot-clé détecté.")
                    return  # Exit the loop to proceed with recording the question
                
        except sr.UnknownValueError:
            phrases = [
    "Je suis toujours la.",
    "Dites mon nom pour commencer.",
    "Vous m'avez oublié ?",
    "Je vous écoute, n'ayez crainte.",
            ]

            # Randomly choose whether to say a phrase or not
            if random.random() < 0.2:  # 1/5 chance
                phrase = random.choice(phrases)
                speak_text(phrase)
        except sr.RequestError as e:
            # Handle API or network issues
            print(f"Erreur de reconnaissance vocale : {e}")
        except Exception as e:
            # Handle other exceptions
            print(f"Une erreur s'est produite : {e}")

def listen():
    File = "VoiceInput.wav"
    
    with sr.Microphone() as source:
        source.pause_threshold = 1
        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
        
        with open(File, "wb") as f:
            f.write(audio.get_wav_data())
    return File

def transcribe_audio_to_text(filename):
    """
    Transcribes audio from a file into text.
    """
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="fr-FR")
    except sr.UnknownValueError:
        return "Null"
    except Exception as e:
        print(f"Erreur pendant la transcription : {e}")
        return "Null"