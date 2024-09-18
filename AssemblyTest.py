# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "ead1f0db1289429d9d42e092867405a3"

# URL of the file to transcribe
FILE_URL = "Wednesday.m4a"

config = aai.TranscriptionConfig(
  speech_model=aai.SpeechModel.best,
  iab_categories=True,
  auto_chapters=True,
  sentiment_analysis=True,
  language_detection=True
)

transcriber = aai.Transcriber(config=config)
transcript = transcriber.transcribe(FILE_URL)

print("------------------sentiment start-----------------")
# Get the parts of the transcript that were tagged with topics MedicalHealth>DiseasesAndConditions>
for result in transcript.iab_categories.results:
    print(result.text)
    print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")
    for label in result.labels:
        print(f"{label.label} ({label.relevance})")

# Get a summary of all topics in the transcript
for topic, relevance in transcript.iab_categories.summary.items():
    print(f"Audio is {relevance * 100}% relevant to {topic}")
print("------------------sentiment end-----------------")

print("------------------chapter start-----------------")
for chapter in transcript.chapters:
  print(f"{chapter.start}-{chapter.end}: {chapter.headline} /n {chapter.summary}")

print("---------------chapter end-----------------")

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)