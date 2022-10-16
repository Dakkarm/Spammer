import pyautogui
import time

time.sleep(3)
f = open("C:\\Users\\Dakkarm\\Desktop\\ProgrammazioneACaso\\Spammer\\TextToSpam.txt", 'r')
for word in f:

    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(3)

