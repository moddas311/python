import pyautogui
from time import sleep

sleep(5)

for i in range(0, 10):
    pyautogui.write('I Love You, Python', interval=0.25)
    pyautogui.press('enter')
    


