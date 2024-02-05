import numpy as np
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
from pydub import AudioSegment
FILTER_SIZE = 15

DISTANCE_FROM_ANCHOR = 0.05
WINDOW_WIDTH = 1.8
WINDOW_HEIGHT = 4000

class FingerprintGenerator:
    
    def generate_spectrogram(file_path):
        sample_rate = 44100
        a = AudioSegment.from_file(file_path).set_channels(1).set_frame_rate(sample_rate)
        audio = np.frombuffer(a.raw_data, np.int16)
        nperseg = int(sample_rate * 0.2)
        return spectrogram(audio, sample_rate, nperseg=nperseg)

    def extract_peaks(matrix, frequencies, time_instances):
        max_filtered_data = maximum_filter(matrix, size=FILTER_SIZE, mode='constant', cval=0.0)
        is_peak = (matrix == max_filtered_data) 
        peak_rows, peak_cols = is_peak.nonzero()
        peak_values = matrix[peak_rows, peak_cols]
        sorted_indices = peak_values.argsort()[::-1]
        sorted_peak_coordinates = [(peak_rows[idx], peak_cols[idx]) for idx in sorted_indices]
        total_pixels = matrix.shape[0] * matrix.shape[1]
        target_peak_count = int((total_pixels / (FILTER_SIZE**2)) * 0.8)
        selected_peaks = sorted_peak_coordinates[:target_peak_count]
        return np.array([(frequencies[row], time_instances[col]) for row, col in selected_peaks])
    
    def target_window(center, data_points, width, height, time_offset):
        x_start = center[1] + time_offset
        x_end = x_start + width
        y_start = center[0] - (height * 0.5)
        y_end = y_start + height
        return [data_point for data_point in data_points if y_start <= data_point[0] <= y_end and x_start <= data_point[1] <= x_end]
        
    def hash_points(points):
        hashes = {}
        for anchor in points:
            for target in FingerprintGenerator.target_window(anchor, points, WINDOW_WIDTH, WINDOW_HEIGHT, DISTANCE_FROM_ANCHOR):
                hashed = hash((anchor[0], target[0], target[1] - target[1]))
                hashes[hashed] = anchor[1]
        return hashes

    def generate_fingerprint(file_path):
        f, t, Sxx = FingerprintGenerator.generate_spectrogram(file_path)
        peaks = FingerprintGenerator.extract_peaks(Sxx, f, t)
        fingerprint = FingerprintGenerator.hash_points(peaks)
        return fingerprint