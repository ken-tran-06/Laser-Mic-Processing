import numpy as np
import csv
import wave
from pathlib import Path

def normalize_to_int16(samples):
    peak = np.max(np.abs(samples)) # Gets Peaks or Trough From The Sound Wave

    # Avoid dividing by zero on a silent signal
    if peak == 0:
        return np.zeros(len(samples),  dtype = np.int16)

    # Scale to -1.0 .. 1.0, then to the 16-bit range
    scaled = samples/peak
    scaled = np.round(scaled*32767)

    # 3. Cast to 16-bit integers after scaling
    return scaled.astype(np.int16)

def write_wav(filename, samples, sample_rate=8000):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)           # mono
        wf.setsampwidth(2)           # 2 bytes = 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(samples.tobytes())

def remove_dc_offset(samples):
    # 1. Calculate the average of the samples
    mean = np.mean(samples)

    # 2. Subtract that average from every sample
    center = samples - mean # Takes every value in the samples array in subtract mean

    # 3. Return the centered samples
    return center

def load_data(filename):
    values = []

    # Open the CSV file
    with open(filename, newline= "") as f:
        reader = csv.reader(f)
        # samples = load_data("data/test_signal.csv")

        # Skip the header
        next(reader)
        # Extract adc_value from each row
        for row in reader:
            values.append(int(row[1]))

    # Convert the values into a NumPy array
    return np.array(values)

# MAIN
samples = load_data("data/test_signal.csv")
centered = remove_dc_offset(samples)
audio = normalize_to_int16(centered)

print(audio[:10])
write_wav("output/test_signal.wav", audio, sample_rate=8000)