import openai

def generate_explanation_from_transcription(api_key, transcription, model="gpt-4o"):
    """
    Genera una spiegazione intuitiva del testo trascritto utilizzando GPT.

    :param transcription: Testo trascritto da Whisper.
    :param model: Modello GPT da utilizzare (es. "gpt-4o").
    :return: Spiegazione intuitiva del contenuto.
    """
    # Imposta la chiave API di OpenAI
    openai.api_key = api_key

    prompt = (
        "Ti fornisco una trascrizione di una conversazione:\n\n"
        f"{transcription}\n\n"
        "Crea una spiegazione intuitiva, chiara e sintetica di ciò di cui si parla nella conversazione, "
        "mettendo in evidenza i punti principali e rendendoli facilmente comprensibili."
    )

    # Richiesta all'API OpenAI
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sei un assistente esperto nel sintetizzare informazioni."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
