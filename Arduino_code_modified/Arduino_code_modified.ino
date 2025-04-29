#include <Servo.h>

Servo finger1;  // Create Servo objects for each finger
Servo finger2;
Servo finger3;
Servo finger4;
Servo finger5;

void setup() {
    finger1.attach(9);  // Attach servos to PWM pins
    finger2.attach(10);
    finger3.attach(11);
    finger4.attach(6);  // Adjust pin numbers as needed
    finger5.attach(5);

    Serial.begin(9600);  // Start serial communication
}

void loop() {
    if (Serial.available()) {
        String data = Serial.readStringUntil('\n');
        int fingerIndex = data.substring(0, 1).toInt();
        int isUp = data.substring(2).toInt();

        moveFinger(fingerIndex, isUp);
    }
}

void moveFinger(int fingerIndex, int isUp) {
    switch (fingerIndex) {
        case 0:
            finger1.write(isUp ? 180 : 0);
            break;
        case 1:
            finger2.write(isUp ? 180 : 0);
            break;
        case 2:
            finger3.write(isUp ? 180 : 0);
            break;
        case 3:
            finger4.write(isUp ? 180 : 0);
            break;
        case 4:
            finger5.write(isUp ? 180 : 0);
            break;
    }
}
