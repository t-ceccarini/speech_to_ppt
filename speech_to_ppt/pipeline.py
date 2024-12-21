import os
from speech_to_ppt.transcription import transcribe_audio
from speech_to_ppt.presentation import generate_presentation_from_transcription, generate_presentation_with_template
from speech_to_ppt.explanation import generate_explanation_from_transcription

# Configurazione del percorso
RAW_DATA_DIR = "data/raw/"
PROCESSED_DATA_DIR = "data/processed/"
REFERENCES_DIR = "references/"
EXPLANATION_DIR = "data/explanations/"
PRESENTATION_DIR = "data/presentations/"
AUDIO_FILE = "acea nelle puntate precedenti.mp3"
TEMPLATE_FILE = "template.pptx"
OUTPUT_TRANSCRIPTION = "trascrizione.txt"
OUTPUT_EXPLANATION = "explanation.txt"
OUTPUT_PRESENTATION = "presentazione.pptx"

def main(api_key, audio_file):
    # Percorsi dei file
    audio_path = os.path.join(RAW_DATA_DIR, audio_file)
    transcription_path = os.path.join(PROCESSED_DATA_DIR, OUTPUT_TRANSCRIPTION)
    explanation_path = os.path.join(EXPLANATION_DIR, OUTPUT_EXPLANATION)
    template_path = os.path.join(REFERENCES_DIR, TEMPLATE_FILE)
    presentation_path = os.path.join(PRESENTATION_DIR, OUTPUT_PRESENTATION)
    
    # Step 1: Trascrivi il file audio
    transcription = transcribe_audio(audio_path)
    with open(transcription_path, "w", encoding='utf-8') as f:
        f.write(transcription)
    print(f"Trascrizione salvata in: {transcription_path}")
    
    # Step 2: Generazione di una spiegazione intuitiva
    explanation = generate_explanation_from_transcription(api_key, transcription)
    with open(explanation_path, "w", encoding="utf-8") as file:
        file.write(explanation)
    print(f"Spiegazione salvata in: {explanation_path}")

    # Contenuti della presentazione
    slides_content = [
        {"type": "title", "title": "Benvenuti", "content": "Introduzione alla presentazione"},
        {"type": "content", "title": "Argomento 1", "content": "Questo è il primo argomento trattato."},
        {"type": "graph", "title": "Analisi dei dati", "content": "Grafici e risultati qui."}
    ]

    # Step 3: Genera la presentazione PowerPoint
    generate_presentation_from_transcription(api_key, explanation, presentation_path)
    print(f"Presentazione salvata in: {presentation_path}")

if __name__ == "__main__":
    # Inserisci la tua chiave API di OpenAI
    API_KEY = ""
    main(API_KEY, AUDIO_FILE)
