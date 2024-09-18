from google.cloud import speech_v1p1beta1 as speech
def transcribe_long_audio_gcs(gcs_uri):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=22050,  # Set the correct sample rate for your audio
        language_code="ta-IN",  # Tamil language code
    )

    # Asynchronous request
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")

    # Wait for the operation to complete (can take some time depending on file length)
    response = operation.result(timeout=600)

    # Print the transcription
    for result in response.results:
        print("Transcript in Tamil: {}".format(result.alternatives[0].transcript))

if __name__ == "__main__":
    # GCS URI of your audio file
    gcs_uri = "gs://jarsis_media/audio/cleaned_audio.wav"
    transcribe_long_audio_gcs(gcs_uri)
