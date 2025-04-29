# import cv2
# import cvzone
# import serial  # For serial communication
# from cvzone import HandTrackingModule
#
# # Serial communication setup
# arduino = serial.Serial('COM10', 9600)  # Adjust COM port if needed
#
# # Hand detector
# detector = HandTrackingModule.HandDetector(detectionCon=0.8, maxHands=1)
#
# # Video capture
# cap = cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)
#
#     if hands:
#         hand = hands[0]
#         fingers = detector.fingersUp(hand)
#         fingerCount = len(fingers)
#
#         # Send finger count to Arduino
#         arduino.write(str(fingerCount).encode())
#         print(fingers)
#
#     # Display video with hand landmarks (optional)
#     cv2.imshow("Image", img)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import cv2
import cvzone
import serial  # For serial communication
from cvzone import HandTrackingModule

# Serial communication setup with try-except for error handling
try:
    arduino = serial.Serial('COM10', 9600)  # Adjust COM port if needed
    arduino_connected = True
    print("Arduino connected")
except serial.SerialException as e:
    arduino_connected = False
    print("Arduino not connected:", e)

# Hand detector
detector = HandTrackingModule.HandDetector(detectionCon=0.8, maxHands=1)

# Video capture
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        fingerCount = len(fingers)

        # Send finger count to Arduino only if it's connected
        if arduino_connected:
            arduino.write(str(fingers).encode())
        print(str(fingers).encode())

    # Display video with hand landmarks (optional)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
