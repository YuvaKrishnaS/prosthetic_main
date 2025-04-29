// we first import our libraries

#include "cvzone.h"    // this help us to communicate with python over the serial com port

#include "Servo.h"
Servo servo;                         // create our servo object
SerialData data(1,3);                // create our serial object
int value[2];                   //create an array to store our received values

void setup () {
  
  data.begin(9600);   // begin our serial communication
  servo.attach(9);     // connect our servo pin
}

void loop () {
  data.Get(value);         // read the value from python and store it in value
  servo.write(value[0]);      // since our received value is an array, we only accept the first value since only one servo is attached
  
  delay(30);   // delay for 30 milli seconds

  // All done 
  // lets move to python 
}
