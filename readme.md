# Prosthetic Hand Control Using OpenCV, Arduino, and Python

This project is a prototype for a low-cost prosthetic hand designed to assist individuals with limited access to expensive prosthetic solutions. The system leverages computer vision (OpenCV), Arduino microcontrollers, and Python to provide basic hand gesture recognition and control.

## Features
- **Hand Gesture Recognition**: Uses OpenCV to detect and interpret hand gestures.
- **Arduino Integration**: Controls servo motors to mimic hand movements.
- **Low-Cost Design**: Built with affordable and accessible components.
- **Customizable**: Easily adaptable for different use cases and hardware configurations.

## Requirements
- Python 3.10
- OpenCV library
- Arduino IDE
- Required hardware:
    - Arduino board (e.g., Arduino Uno)
    - Servo motors
    - Webcam
    - Power supply
    - 3D-printed or pre-built prosthetic hand frame

## Installation
1. Clone the repository:
     ```bash
     git clone https://github.com/YuvaKrishnaS/prosthetic_main.git
     ```
2. Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
3. Upload the Arduino code to your Arduino board using the Arduino IDE.

## Usage
1. Connect the hardware components as per the circuit diagram provided in the repository.
2. Run the Python script to start the hand gesture recognition:
     ```bash
     python hand_control.py
     ```
3. The system will detect hand gestures via the webcam and control the prosthetic hand accordingly.

## File Structure
- `hand_control.py`: Main Python script for gesture recognition and communication with Arduino.
- `arduino_code/`: Contains the Arduino sketch for controlling the servo motors.
- `requirements.txt`: Python dependencies.
- `docs/`: Additional documentation and circuit diagrams.

## Important Git Commands
- Clone a repository:
    ```bash
    git clone <repository-url>
    ```
- Check the status of your repository:
    ```bash
    git status
    ```
- Add changes to the staging area:
    ```bash
    git add <file-name>
    ```
- Commit changes:
    ```bash
    git commit -m "Your commit message"
    ```
- Push changes to the remote repository:
    ```bash
    git push origin <branch-name>
    ```
- Pull the latest changes from the remote repository:
    ```bash
    git pull origin <branch-name>
    ```
- Create a new branch:
    ```bash
    git branch <branch-name>
    ```
- Switch to a branch:
    ```bash
    git checkout <branch-name>
    ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to the open-source community for providing the tools and resources that made this project possible.