#include <Arduino.h>

constexpr uint8_t TX = 3;
constexpr uint8_t TX_MUX[] = { 7, 5, 16, 14 }; // S0 -> S3
constexpr uint8_t RX[] = { /*4,*/ 6, 8, 21, 20, 19, 18, 10, 9};

uint8_t mask = 0b0001;
uint8_t channel = 0;

void select_pwm_channel(const uint8_t& channel){
  mask = 0b0001;
  for (const auto& pin: TX_MUX){
    digitalWrite(pin, static_cast<uint8_t>((channel & mask)==0));
    mask <<= 1;
  }
}

void setup() {
  Serial.begin(0);
  for (const auto& pin: TX_MUX){ pinMode(pin, OUTPUT); }
  for (const auto& pin: RX){ pinMode(pin, INPUT); }

  pinMode(TX,OUTPUT);
  TCCR0A = (COM0A0) | _BV(COM0B1) | _BV(WGM01) | _BV(WGM00);
  TCCR0B = _BV(WGM02) | _BV(CS00);
  OCR0A = 3;
  OCR0B = 1;
  // analogReference(INTERNAL);         //change reference to 1.1V
}

void loop() {
  for (channel = 0; channel < (1 << 4); ++channel){
    select_pwm_channel(channel);
    Serial.print(channel);
    for (const auto &pin : RX){
      Serial.print(",");
      Serial.print(analogRead(pin));
    }
    Serial.println();
  }
}