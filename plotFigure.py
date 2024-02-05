import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

def plot_wave(file_path, save_path):
    sample_rate, audio_data = wavfile.read(file_path)
    time = [i / sample_rate for i in range(len(audio_data))]
    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_data, color='b')
    plt.title('Waveform of the Audio Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.savefig(save_path, format='png', bbox_inches='tight')
    plt.show()

def plot_spectrogram(t, f, Sxx):
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.title('Spectrogram')
    plt.colorbar(label='Power/Frequency (dB/Hz)')
    plt.savefig('spectrogram.png', format='png', bbox_inches='tight')
    plt.show()

def plot_score_istogram(scores):
    categories = list(scores.keys())
    values = list(scores.values())
    # Plotting a bar graph (isogram)
    plt.figure(figsize=(10, 4))
    plt.bar(categories, values)
    plt.xlabel('Time difference')
    plt.ylabel('Matches')
    plt.title('Best match')
    plt.savefig('score_istogram.png', format='png', bbox_inches='tight')
    plt.show() 
