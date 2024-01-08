from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(10)

text = ""

with open("instance.txt") as f:
    for line in f.readlines():
        text += line


for char in text:
    if char == "\n":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        keyboard.press(char)
        keyboard.release(char)
    time.sleep(0.12)

time.sleep(10)

text = ""

with open("main.txt") as f:
    for line in f.readlines():
        text += line


for char in text:
    if char == "\n":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        keyboard.press(char)
        keyboard.release(char)
    time.sleep(0.12)
