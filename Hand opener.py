import cv2
import serial
from cvzone.HandTrackingModule import HandDetector
import mediapipe

# Serial communication setup with try-except for error handling
try:
    arduino = serial.Serial('COM10', 9600)  # Adjust COM port if needed
    arduino_connected = True
    print("Arduino connected")
except serial.SerialException as e:
    arduino_connected = False
    print("Arduino not connected:", e)
# Initialize the hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture the frame
    success, img = cap.read()

    if not success:
        print("Failed to capture video")
        break

    # Detect the hand and its landmarks
    hands, img = detector.findHands(img, draw=True)  # Draw hand landmarks

    if hands:
        # Get the first detected hand
        hand = hands[0]

        # Detect which fingers are up
        fingers = detector.fingersUp(hand)

        # Format the data string as "$11111" (without commas)
        data_to_send = f"${''.join(map(str, fingers))}"
        print("Sending data to Arduino:", data_to_send)

        # Send the formatted data to the Arduino
        arduino.write(data_to_send.encode())

    # Display the video frame
    cv2.imshow("Hand Tracking", img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
