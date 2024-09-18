from google.cloud import speech_v1p1beta1 as speech

def transcribe_gcs(gcs_uri):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=32000,
        language_code="ta-IN",
    )

    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=10000)
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

if __name__ == "__main__":
    #gcs_uri = "gs://jarsis_media/audio/PizerTest.mp3"  # Replace with your GCS URI
    gcs_uri = "gs://jarsis_media/audio/Wednesday.m4a"  # Replace with your GCS URI
    transcribe_gcs(gcs_uri)