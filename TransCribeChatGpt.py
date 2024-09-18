import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "ead1f0db1289429d9d42e092867405a3"
transcriber = aai.Transcriber()
supported_languages_for_best = {
    "en",
    "es",
    "fr",
    "de",
    "it",
    "pt",
    "nl",
    "hi",
    "ja",
    "zh",
    "fi",
    "ko",
    "pl",
    "ru",
    "tr",
    "uk",
    "vi",
}
def detect_language(audio_url):
    config = aai.TranscriptionConfig(
        audio_end_at=60000,  # first 60 seconds (in milliseconds)
        language_detection=True,
        speech_model=aai.SpeechModel.nano,
    )
    transcript = transcriber.transcribe(audio_url, config=config)
    return transcript.json_response["language_code"]

def transcribe_file(audio_url, language_code):
    config = aai.TranscriptionConfig(
        language_code=language_code,
        speech_model=(
            aai.SpeechModel.best
            if language_code in supported_languages_for_best
            else aai.SpeechModel.nano
        ),
    )
    transcript = transcriber.transcribe(audio_url, config=config)
    return transcript

    # "https://storage.googleapis.com/aai-web-samples/public_benchmarking_portugese.mp3",
    # "https://storage.googleapis.com/aai-web-samples/public_benchmarking_spanish.mp3",
    # "https://storage.googleapis.com/aai-web-samples/slovenian_luka_doncic_interview.mp3",
    # "https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3",

audio_urls = [
    "Wednesday.ma4"
]

for audio_url in audio_urls:
    language_code = detect_language(audio_url)
    print("Identified language:", language_code)

    transcript = transcribe_file(audio_url, language_code)
    print("Transcript:", transcript.text[:1000], "...")