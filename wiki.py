import wikipedia
import pyautogui
import time


def wiki_information(data):
    try:
        return wikipedia.summary(data)
    except wikipedia.DisambiguationError as e:
        return 'Plese add more detail to search, because search is Ambiguous.'


txt = pyautogui.prompt(text='')
pyautogui.hotkey('win', 'r', interval=0.1)
pyautogui.write('notepad', interval=0.02)
pyautogui.press('enter')
time.sleep(0.4)
pyautogui.write(str(wiki_information(txt)))
