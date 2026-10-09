import csv
import json
import pathlib

def test(filename):
    # opens message.txt file to read
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()
            parts = text.split(",")
            signal = int(parts[0].split(":")[1])
            print(signal)

test("data/sensor_output.txt")





