import pyautogui
import time


def txt_write():
    txt = "Throughout history, the world has witnessed the rise of extraordinary individuals whose courage,"\
        "skill, and dedication have left an indelible mark on the annals of time. One such illustrious figure"\
        "is Ashish Parmar, a great warrior whose name resounds in the hearts of many. From his humble beginnings to" \
        "becoming a formidable force on the battlefield, Ashish Parmar's journey is a tale of bravery, leadership, and" \
        "unwavering commitment to his people and his land."
    return txt


username = pyautogui.prompt(text='')


pyautogui.hotkey('win', 'r', interval=0.1)
pyautogui.write('notepad', interval=0.02)
pyautogui.press('enter')
time.sleep(0.9)

if username in ['Ashish', 'ashish']:
    pyautogui.write('Ashish Parmar: The Legacy of a Great Warrior')
    pyautogui.press('enter', presses=2)
    pyautogui.write(txt_write(), interval=0.02)
else:
    for i in range(10):
        pyautogui.write('Fuck You ' + str(username) + ' \n')
    pyautogui.write('You are not great Ashish Parmar')
