from google.cloud import speech_v1p1beta1 as speech

# Set up the client
gcs uri = speech.SpeechClient()

# Define the path to the audio file in your GCS bucket
gcs_uri = "gs://jarsis_media/audio/cleaned_audio.wav"

# Configure the audio file and recognition config
audio = speech.RecognitionAudio(uri=gcs_uri)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # or the correct encoding
    sample_rate_hertz=22050,  # Set the sample rate of your file
    language_code="ta-IN",  # Tamil language code
    enable_automatic_punctuation=True
)

# Use asynchronous recognition
operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = operation.result(timeout=600)  # Wait for the result with a timeout

# Print out the transcription result
for result in response.results:
    print("Transcription: {}".format(result.alternatives[0].transcript))
