/*
  Analog input, analog output, serial output

 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.

 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground

 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin0 = A0;  // Analog input pin that the potentiometer is attached to
const int analogInPin1 = A1;  // Analog input pin that the potentiometer is attached to
const int analogInPin2 = A2;  // Analog input pin that the potentiometer is attached to
const int analogInPin3 = A3;  // Analog input pin that the potentiometer is attached to


int sensor1Value = 0;        // value read from the pot
int sensor2Value = 0;        // value output to the PWM (analog out)
int sensor3Value = 0;        // value output to the PWM (analog out)
int sensor4Value = 0;        // value output to the PWM (analog out)
int inDelay = 0;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
}

void loop() {
  // read the analog in value:
  sensor1Value = analogRead(analogInPin0);
  sensor2Value = analogRead(analogInPin1);
  sensor3Value = analogRead(analogInPin2);
//  sensor4Value = analogRead(analogInPin3);
//
//  inDelay = map(sensor4Value,0,1023,15,21);
//
//  switch (inDelay){
//    case 15:
//      digitalWrite(8,LOW);
//      digitalWrite(7,LOW);
//      digitalWrite(6,LOW);
//      digitalWrite(5,LOW);
//      digitalWrite(4,LOW);
//      digitalWrite(3,LOW);
//      digitalWrite(2,HIGH);
//      
//    break;
//      
//    case 16:
//      digitalWrite(8,LOW);
//      digitalWrite(7,LOW);
//      digitalWrite(6,LOW);
//      digitalWrite(5,LOW);
//      digitalWrite(4,LOW);
//      digitalWrite(3,HIGH);
//      digitalWrite(2,HIGH);
//    break;
//      
//    case 17:
//      digitalWrite(8,LOW);
//      digitalWrite(7,LOW);
//      digitalWrite(6,LOW);
//      digitalWrite(5,LOW);
//      digitalWrite(4,HIGH);
//      digitalWrite(3,HIGH);
//      digitalWrite(2,HIGH);
//    break;
//
//    case 18:
//      digitalWrite(8,LOW);
//      digitalWrite(7,LOW);
//      digitalWrite(6,LOW);
//      digitalWrite(5,HIGH);
//      digitalWrite(4,HIGH);
//      digitalWrite(3,HIGH);
//      digitalWrite(2,HIGH);
//    break;
//
//    case 19:
//      digitalWrite(8,LOW);
//      digitalWrite(7,LOW);
//      digitalWrite(6,HIGH);
//      digitalWrite(5,HIGH);
//      digitalWrite(4,HIGH);
//      digitalWrite(3,HIGH);
//      digitalWrite(2,HIGH);
//    break;
//
//    case 20:
//      digitalWrite(8,LOW);
//      digitalWrite(7,HIGH);
//      digitalWrite(6,HIGH);
//      digitalWrite(5,HIGH);
//      digitalWrite(4,HIGH);
//      digitalWrite(3,HIGH);
//      digitalWrite(2,HIGH);
//    break;
//
//    case 21:
//      digitalWrite(8,HIGH);
//      digitalWrite(7,HIGH);
//      digitalWrite(6,HIGH);
//      digitalWrite(5,HIGH);
//      digitalWrite(4,HIGH);
//      digitalWrite(3,HIGH);
//      digitalWrite(2,HIGH);
//    break;
//  }

  Serial.print(sensor1Value);
  Serial.print(",");
  Serial.print(sensor2Value);
  Serial.print(",");
  Serial.println(sensor3Value);
//  Serial.print(",");
//  Serial.println(inDelay);
  

  delay(21);
}
