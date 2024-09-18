import os
from google.cloud import speech
from pydub import AudioSegment


# Set the path to your Google Cloud service account key
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_service_account_key.json'

def convert_m4a_to_wav(m4a_file, wav_file):
    # Convert .m4a to .wav using pydub
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(wav_file, format="wav")
    return wav_file

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    # Read the audio file
    with open(audio_file, 'rb') as audio:
        audio_content = audio.read()

    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # WAV encoding
        sample_rate_hertz=32000,  # Ensure this matches the audio file’s sample rate
        language_code='ta-IN',  # Tamil language code
    )

    # Call the API and process the response
    response = client.recognize(config=config, audio=audio)

    # Print the transcription results
    for result in response.results:
        print('Transcription: {}'.format(result.alternatives[0].transcript))

# Example usage
m4a_file_path = 'Wednesday.m4a'
wav_file_path = 'converted_audio.wav'

# Convert .m4a to .wav
converted_wav = convert_m4a_to_wav(m4a_file_path, wav_file_path)
#converted_wav = 'WednesdayNew.m4a'

# Transcribe the converted audio
transcribe_audio(converted_wav)
