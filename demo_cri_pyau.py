import pyautogui
import time
import pyperclip
import webbrowser

# Safety pause between actions
pyautogui.PAUSE = 1

# Allow time to switch focus
print("Starting in 5 seconds...")
time.sleep(5)

# -----------------------------
# Step 1: Open browser (default)
# -----------------------------
webbrowser.open("https://www.google.com")

# Wait for browser to load
time.sleep(7)

# -----------------------------
# Step 2: Search query
# -----------------------------
search_text = "t20 world cup status"

# Copy text to clipboard (more reliable than typing)
pyperclip.copy(search_text)

# Focus search bar (Google auto-focuses usually)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Wait for results page
time.sleep(7)

# -----------------------------
# Step 3: Click first result
# -----------------------------
# Press TAB multiple times to reach first result
# (number may vary slightly by browser)

for _ in range(5):
    pyautogui.press("tab")

pyautogui.press("enter")

print("Done!")