import cv2
import serial
import threading
from tkinter import Tk, Button, Label
from cvzone.HandTrackingModule import HandDetector
from PIL import Image, ImageTk

class HandTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Tracking GUI")

        # State variables
        self.switch_states = [0] * 5  # States for five switches (0 = closed, 1 = open)
        self.camera_mode = False  # False = Switch Mode, True = Camera Mode
        self.running = False

        # Serial communication setup
        try:
            self.arduino = serial.   Serial('COM10', 9600)
        except Exception as e:
            print(f"Error connecting to Arduino: {e}")
            self.arduino = None

        # GUI Components
        self.buttons = []
        for i in range(5):
            button = Button(root, text=f"Finger {i+1}: OFF", bg="red", command=lambda i=i: self.toggle_switch(i))
            button.grid(row=0, column=i)
            self.buttons.append(button)

        self.mode_button = Button(root, text="Switch to Camera Mode", command=self.toggle_mode)
        self.mode_button.grid(row=1, column=2)

        self.status_label = Label(root, text="Mode: Switch Mode", font=("Arial", 14))
        self.status_label.grid(row=2, column=0, columnspan=5)

        self.video_label = Label(root)
        self.video_label.grid(row=3, column=0, columnspan=5)

        # Hand Tracking Components
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)
        self.cap = None

    def toggle_switch(self, finger_index):
        # Toggle the switch state
        self.switch_states[finger_index] = 1 - self.switch_states[finger_index]
        state = "ON" if self.switch_states[finger_index] else "OFF"
        color = "green" if self.switch_states[finger_index] else "red"
        self.buttons[finger_index].config(text=f"Finger {finger_index + 1}: {state}", bg=color)
        self.send_to_arduino()

    def toggle_mode(self):
        # Switch between Camera Mode and Switch Mode
        self.camera_mode = not self.camera_mode
        mode_text = "Camera Mode" if self.camera_mode else "Switch Mode"
        button_text = "Switch to Switch Mode" if self.camera_mode else "Switch to Camera Mode"
        self.status_label.config(text=f"Mode: {mode_text}")
        self.mode_button.config(text=button_text)

        if self.camera_mode:
            # Start camera thread
            self.running = True
            self.cap = cv2.VideoCapture(0)
            threading.Thread(target=self.camera_tracking).start()
        else:
            # Stop camera thread
            self.running = False
            if self.cap:
                self.cap.release()
                self.cap = None
            self.video_label.config(image="")

    def camera_tracking(self):
        while self.running:
            success, img = self.cap.read()
            if not success:
                break

            hands, img = self.detector.findHands(img, draw=True)
            if hands:
                hand = hands[0]
                fingers = self.detector.fingersUp(hand)
                data_to_send = f"${''.join(map(str, fingers))}"
                if self.arduino:
                    self.arduino.write(data_to_send.encode())

            # Convert frame to Tkinter-compatible format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        if self.cap:
            self.cap.release()

    def send_to_arduino(self):
        # Convert switch states to binary and send to Arduino
        if not self.camera_mode:  # Only send in Switch Mode
            data_to_send = f"${''.join(map(str, self.switch_states))}"
            print("Sending data to Arduino:", data_to_send)
            if self.arduino:
                self.arduino.write(data_to_send.encode())

    def on_closing(self):
        # Graceful shutdown
        self.running = False
        if self.cap:
            self.cap.release()
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
        self.root.destroy()

# Create Tkinter window and run the app
root = Tk()
app = HandTrackingApp(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()
