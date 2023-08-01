import pyautogui

print(pyautogui.position())
pyautogui.click(609, 748, duration=0.9)
pyautogui.click(754, 313, duration=0.9)
pyautogui.click(155, 44, duration=0.8)
pyautogui.write('www.youtube.com', interval=0.1)
pyautogui.keyDown('enter')
pyautogui.click(388, 135, interval=0.6, duration=0.5)
pyautogui.write('xing xing', interval=0.3)
pyautogui.click(901, 146, duration=0.2)
