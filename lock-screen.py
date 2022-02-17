"""lock-screen.py

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

# blur the image
blurImg = cv2.blur(image, (30,30))

# write to the disk using opencv
cv2.imwrite(sys.argv[1], blurImg)
