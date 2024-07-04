import sounddevice as sd
import wavio

# Parameters
duration = 5  # seconds
fs = 44100  # Sample rate

print("Recording...")
# Record audio
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print("Recording finished")

# Save the recording as a WAV file
wavio.write("my_recording.wav", recording, fs, sampwidth=2)
print("Recording saved as 'my_recording.wav'")
