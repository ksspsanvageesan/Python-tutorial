import pyautogui
import time

pyautogui.click(100,100)  # Click to focus on the desktop
time.sleep(2)  # Wait for the click to register
pyautogui.rightClick(100,100)  # Right-click to open context menu
time.sleep(10)  # Wait for the context menu to open


x,y=pyautogui.position()  # Get the current mouse position
print(f"Current mouse position: ({x}, {y})")  # Print the current mouse position


pyautogui.drag(100,100,200,200)

pyautogui.scrollDown(500)  # Scroll down 500 units
pyautogui.scrollUp(500)  # Scroll up 500 units
pyautogui.moveTo(500, 500)  # Move the mouse to (500, 500)