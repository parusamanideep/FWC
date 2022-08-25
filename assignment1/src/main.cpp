#include <Arduino.h>
int P,Q,R,S,F;

void setup() {
    pinMode(2, INPUT);  //P
    pinMode(3, INPUT);  //Q
    pinMode(4, INPUT);  //R
    pinMode(5, INPUT);  //S
    pinMode(13, OUTPUT); //F
  }

void loop() {
  P = digitalRead(2);
  Q = digitalRead(3);
  R = digitalRead(4);
  S = digitalRead(5);

  F = (!P&&!Q) || (!P&&S) || (R&&!S) || (Q&&R);
  digitalWrite(13,F);
}
