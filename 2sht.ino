#include <Sensirion.h>

//INITIAL AUTHOR: Erin Osler (2018, CU-ITK)
//This code is uploaded to the arduino and will record temperature and humidity data from two SHT75 sensors connected according to the clockpins below (dewpoint not used)

const uint8_t dataPin_1 = 10;
const uint8_t clockPin_1 = 12;
const uint8_t dataPin_2 = 8;
const uint8_t clockPin_2 = 4;

Sensirion sensor_1 = Sensirion(dataPin_1, clockPin_1);
Sensirion sensor_2 = Sensirion(dataPin_2, clockPin_2);

float temp_1;
float humid_1;
float temp_2;
float humid_2;
float dew_1;
float dew_2;

void setup() {
  Serial.begin(9600);
  delay(15);
}

void loop() {
  sensor_1.measure(&temp_1, &humid_1, &dew_1);
  sensor_2.measure(&temp_2, &humid_2, &dew_2);
  
  Serial.print("1:");
  Serial.print(temp_1);
  Serial.print(":");
  Serial.print(humid_1);
  Serial.print("\n");
  
  Serial.print("2:");
  Serial.print(temp_2);
  Serial.print(":");
  Serial.print(humid_2);
  Serial.print("\n");

  delay(5000);
}
