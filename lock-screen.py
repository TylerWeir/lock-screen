"for files in os.listdir("dataset3"):
    if os.path.exists("dataset"):
        os.system("rm -rf "+"dataset")""lock-screen.py

Creates a blurred screenshot of the current desktop and
saves the image to the specified destination."""

import sys
import numpy as np
import cv2
import pyautogui

# take the screenshot using pyautogui
image = pyautogui.screenshot()

# pyautogui gets a PIL image in RGB.  We need to convert it to a numpy 
# array and BGR
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# blur the image a couple times
for i in range(1, 7):
    image = cv2.blur(image, (i*10,i*10))

# write to the disk using opencv
cv2.imwrite(sys.argv[1], image)
