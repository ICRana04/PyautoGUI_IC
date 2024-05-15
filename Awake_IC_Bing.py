import pyautogui
import time
import sys
from datetime import datetime

# Disable the failsafe feature of pyautogui
pyautogui.FAILSAFE = False

# Parse command-line arguments
numSec = None
if ((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
    # If no valid argument provided, default to 30 seconds
    numSec = 30
else:
    # Otherwise, use the provided argument as the interval in seconds
    numSec = int(sys.argv[1])

while True:
    x = 0
    while x < numSec:
        # Wait for numSec seconds
        time.sleep(1)
        x += 1

    # Move the mouse cursor along the vertical axis
    for i in range(0, 200):
        pyautogui.moveTo(0, i * 4)

    # Move the mouse cursor to the center of the screen
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2, screen_height // 2)

    # Print a message indicating the time of the movement made
    print("Movement made at {}".format(datetime.now().time()))
