import csv
import json
import math
from pathlib import Path

SAMPLE_RATE = 8000
DURATION = 5
FREQUENCY = 500

# Create the data directory
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Generate ADC samples
samples = []

for n in range(SAMPLE_RATE * DURATION):
    value = 250 + 100 * math.sin(
        2 * math.pi * FREQUENCY * n / SAMPLE_RATE
    )
    samples.append(round(value))

# Save the CSV
with open(data_dir / "test_signal.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sample_index", "adc_value"])

    for index, value in enumerate(samples):
        writer.writerow([index, value])

# Save matching metadata
metadata = {
    "sample_rate_hz": SAMPLE_RATE,
    "adc_bits": 10,
    "sample_count": len(samples),
    "duration_seconds": DURATION
}

with open(data_dir / "test_signal_metadata.json", "w") as file:
    json.dump(metadata, file, indent=2)

print("Test signal generated successfully!")