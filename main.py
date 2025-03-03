from cv2 import cv2
import os
import keyboard
import time
import pyautogui
from random import randint
import threading

def camera():
  cam = cv2.VideoCapture(0)
  while True:
  ret, img = cam.read()
  cv2.imshow("camera", img)
  if cv2.waitKey(10) == 27:
    break
    
  cam.release()
  cv2.destroyAllWindows()

def move():
    screen_width, screen_height = pyautogui.size()
    move_time = 60
    start_time = time.time()
    while time.time() - start_time < move_time:
        x = randint(0, screen_width)
        y = randint(0, screen_height)
        
        pyautogui.moveTo(x, y, duration = 0.1)
    
    pyautogui.moveTo(screen_width // 2, screen_height // 2, duration = 0.5)

def block_input():
    keyboard.block_key('windows')
    keyboard.block_key('ctrl')
    keyboard.block_key('alt')
    keyboard.block_key('tab')
    keyboard.block_key('esc')
    keyboard.block_key('f4')
    keyboard.block_key('del')
    
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(1, 1)
    
def unblock_input():
    keyboard.unblock_key('windows')
    keyboard.unblock_key('ctrl')
    keyboard.unblock_key('alt')
    keyboard.unblock_key('tab')
    keyboard.unblock_key('esc')
    keyboard.unblock_key('f4')
    keyboard.unblock_key('del')
    
    pyautogui.FAILSAFE = True

def main():
    os.startfile("C:/Windows/system32/cmd.exe")
    time.sleep(2)
    keyboard.write("cd && cd C:\ && echo https://youtu.be/dQw4w9WgXcQ?si=RXnVUJYO8tCaQxOU > ricrol.txt")
    pyautogui.press("enter")
    keyboard.write("ipconfig")
    pyautogui.press("enter")
    time.sleep(2)
    os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
    time.sleep(8)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)
    keyboard.write("https://youtu.be/dQw4w9WgXcQ?si=RXnVUJYO8tCaQxOU")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(7)

if __name__ == "__main__":
    block_input()
    camera()
    main()
    move()
    unblock_input()
