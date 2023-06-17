import speech_recognition as sr
from pydub import AudioSegment

def convert_to_text(mp3_file, txt_file):
    # Conversion du fichier MP3 en WAV
    audio = AudioSegment.from_mp3(mp3_file)
    wav_file = mp3_file[:-4] + ".wav"
    audio.export(wav_file, format="wav")

    # Reconnaissance vocale
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as audio_file:
        audio = recognizer.record(audio_file)

    # Conversion en texte
    text = recognizer.recognize_google(audio, language="fr-FR")

    # Enregistrement du texte dans un fichier .txt
    with open(txt_file, "w") as output_file:
        output_file.write(text)

    print(f"Conversion terminée. Le fichier texte {txt_file} a été créé.")

# Exemple d'utilisation
mp3_file = input("Entrez le chemin du fichier MP3 : ")
txt_file = input("Entrez le chemin du fichier texte de sortie : ")
convert_to_text(mp3_file, txt_file)