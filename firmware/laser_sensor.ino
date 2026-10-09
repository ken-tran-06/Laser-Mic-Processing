const int micPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int minVal = 1023;
  int maxVal = 0;

  unsigned long start = millis();

  // Watch the mic for 50 ms
  while (millis() - start < 50) {
    int v = analogRead(micPin);

    if (v < minVal) minVal = v;
    if (v > maxVal) maxVal = v;
  }

  int peakToPeak = maxVal - minVal;

  // Keep Serial Plotter scale at 0–400
  Serial.print("Signal:");
  Serial.print(peakToPeak);

  Serial.print(",Min:");
  Serial.print(0);

  Serial.print(",Max:");
  Serial.println(500);
}