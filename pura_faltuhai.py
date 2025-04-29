import pyautogui
import time


def get_coordinates():
    """
    This function captures three coordinates where the user places the mouse.
    The user has to press Enter to record each coordinate.
    """
    print("Move your mouse to the desired location and press Enter to record the coordinate.")
    coords = []

    for i in range(4):
        input(f"Position your cursor for Point {i + 1} and press Enter...")  # Wait for user input
        x, y = pyautogui.position()  # Get current mouse position
        coords.append((x, y))  # Store the coordinate
        print(f"Point {i + 1} recorded: ({x}, {y})")  # Print the recorded coordinate

    return coords  # Return the list of coordinates


# Step 1: Capture the coordinates
coordinates = get_coordinates()
print("\nYour recorded coordinates:", coordinates)

# Step 2: Ask user for the number of repetitions
n = int(input("\nEnter the number of times to repeat the clicking cycle: "))

# Step 3: Automate clicking
print("\nClicking will start in 3 seconds... Move your cursor away if needed!")
time.sleep(3)  # Give the user some time before the script starts clicking

for _ in range(n):  # Repeat for the number of cycles given by the user
    for x, y in coordinates:
        pyautogui.click(x, y)  # C
        # lick on the given coordinates
        time.sleep(0.5)  # Small delay between clicks for smooth execution
    print(f"Cycle {_ + 1}/{n} completed. Waiting 5 seconds before the next cycle...")
    time.sleep(5)  # Wait 5 seconds before starting the next cycle

print("\nClicking task completed successfully! 🎯")
