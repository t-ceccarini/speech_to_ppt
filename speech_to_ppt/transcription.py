from openai import OpenAI

def transcribe_audio(audio_path):
    """
    Trascrive un file audio utilizzando Whisper.
    
    :param audio_path: Percorso del file audio.
    :return: Testo trascritto.
    """
    audio_file= open(audio_path, "rb")
    client = OpenAI()
    print("Trascrizione in corso...")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )

    return transcription.text