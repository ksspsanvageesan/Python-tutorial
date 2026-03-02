import pyautogui

import time


time.sleep(5)  # Wait for the Start menu to open

#pyautogui.click(x=100, y=100)  # Adjust coordinates as needed

time.sleep(5)  # Wait for the context menu to open

#pyautogui.rightClick(x=995, y=2360)  # Click to open Notepad

time.sleep(5)  # Wait for Notepad to open

#pyautogui.typewrite('Hello, World!')  # Type "Hello, World!"

#pyautogui.press('enter')  # Press Enter to move to the next line

pyautogui.write('This is an automated message.')  # Type another line

pyautogui.press('enter')  # Press Enter again to create a blank line

pyautogui.hotkey('ctrl', 'a')  # Press Ctrl+S to save the file

