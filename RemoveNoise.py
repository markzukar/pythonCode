import noisereduce as nr
import librosa
import soundfile as sf

# Load your audio file with librosa
y, sr = librosa.load("output_file.wav")

# Perform noise reduction
reduced_noise = nr.reduce_noise(y=y, sr=sr)

# Save the cleaned audio using soundfile
sf.write("cleaned_audio.wav", reduced_noise, sr)
