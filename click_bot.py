import pyautogui
import keyboard
from pynput.mouse import Listener
import time

# List to store the two clicked points
click_positions = []
clicks = 2  # Default is 2 clicks, change this variable if you want more clicks per cycle

# Function to record the clicks
def on_click(x, y, button, pressed):
    if pressed and len(click_positions) < 3:  # If less than two clicks have been recorded
        click_positions.append((x, y))  # Add the coordinates of the click
        print(f"Click recorded at ({x}, {y})")

        # If both clicks have been recorded, print a message and stop the listener
        if len(click_positions) == 3:
            print("Both clicks recorded. The script will simulate the clicks repeatedly.")
            return False  # Stop the listener

# Function to simulate the clicks repeatedly
def simulate_clicks():
    print("Click simulation in progress. Press 'a' to stop.")
    try:
        while True:
            # Check if the 'a' key has been pressed to exit
            if keyboard.is_pressed('a'):
                print("The 'a' key was pressed. Exiting the simulation.")
                break

            # Simulate the click on the two registered points
            for pos in click_positions:
                pyautogui.click(pos)  # Click on the point
                time.sleep(1)  # Short pause between clicks

    except KeyboardInterrupt:
        print("Manually interrupted.")

# Start recording the clicks
time.sleep(3)
print("Click twice to record the points. Then the script will simulate the clicks.")
with Listener(on_click=on_click) as listener:
    listener.join()
time.sleep(3)
# Once the clicks are registered, start the simulation
simulate_clicks()

print("Script finished.")