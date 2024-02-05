import sounddevice as sd
import soundfile as sf
class Record:
    def record_audio(duration, sample_rate=44100):
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        print("Recording finished.")
        return audio_data

    def save_audio(file_path, audio_data, sample_rate):
        sf.write(file_path, audio_data, sample_rate)
        print("audio saved at", file_path)
    
    
