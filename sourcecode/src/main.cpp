#include <Arduino.h>

constexpr uint8_t TX = 5;
constexpr uint8_t TX_MUX[4] = { 7, 16, 14, 15 };
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
  TCCR4A = _BV(COM4A0) | _BV(PWM4A);
  TCCR4B = _BV(PWM4X) | _BV(CS40);
  OCR4C = 4;
  OCR4A = 2;
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