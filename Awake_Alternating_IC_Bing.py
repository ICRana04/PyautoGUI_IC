import pyautogui
import time
import sys
from datetime import datetime

# Disable the failsafe feature of pyautogui
pyautogui.FAILSAFE = False

# Parse command-line arguments
numSec = None
if ((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
    # If no valid argument provided, default to 60 seconds
    numSec = 60
else:
    # Otherwise, use the provided argument as the interval in seconds
    numSec = int(sys.argv[1])

# Define the sequence of movements
movements = ['top-left', 'bottom-left', 'top-right', 'bottom-right']
movement_index = 0

while True:
    x = 0
    while x < numSec:
        # Wait for numSec seconds
        time.sleep(1)
        x += 1

    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Determine the movement based on the current index
    if movements[movement_index] == 'top-left':
        pyautogui.moveTo(0, 0)
    elif movements[movement_index] == 'bottom-left':
        pyautogui.moveTo(0, screen_height)
    elif movements[movement_index] == 'top-right':
        pyautogui.moveTo(screen_width, 0)
    else:  # 'bottom-right'
        pyautogui.moveTo(screen_width, screen_height)

    # Move the mouse cursor along the changed side of the screen
    if movements[movement_index] in ['top-left', 'top-right']:
        for i in range(0, screen_height):
            pyautogui.moveTo(pyautogui.position().x, i)
    else:
        for i in range(screen_height, 0, -1):
            pyautogui.moveTo(pyautogui.position().x, i)

    # Print a message indicating the time of the movement made
    print("Movement made at {}".format(datetime.now().time()))

    # Update the movement index for the next iteration
    movement_index = (movement_index + 1) % len(movements)
