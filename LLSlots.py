from PIL import ImageGrab
import pyautogui
import math
import random
import time
import keyboard

def time_noise(t, L):
    # randomly samples time increase/delay
    l = random.uniform(-L, L)
    return t + l

def circle_noise(x, y, R):
    # randomly samples a point in a circle region
    theta = random.uniform(0,math.pi)
    r = random.uniform(0, R)
    x = x + r * math.cos(theta)
    y = y + r * math.sin(theta)
    x = math.floor(x)
    y = math.floor(y)
    return [x, y]

def get_pixel_color(x, y):
    # Take screenshot of the entire screen
    img = ImageGrab.grab()
    # Get RGB at (x, y)
    return img.getpixel((x, y))


def main():
    print("starting...")

    t0 = time.time()
    tf = time.time()
    elapsed = tf - t0
    daySeconds = 24 * 3600
    t = 0.5  # base time delay
    L = 0.1  # time noise level
    R = 6    # position noise level

    while True:
        tf = time.time()
        elapsed = tf - t0
        elapsed = elapsed % daySeconds
        
        bBreak = False
        while elapsed > 8 * 3600: 
            tf = time.time()
            elapsed = tf - t0
            elapsed = elapsed % daySeconds
            pyautogui.click(974, 698)
            time.sleep(t)
            pyautogui.click(714, 911)
            time.sleep(t)
            
            if keyboard.is_pressed('esc'):
                print("Stopping...")
                bBreak = True
                break
        if bBreak:
            print("Stopping...")
            break

        print("Clicking...")
        pyautogui.click(1664, 959)
        time.sleep(t)
        pyautogui.click(1468, 251)
        time.sleep(t)
        

        
        if keyboard.is_pressed('esc'):
            print("Stopping...")
            break
    print("returning...")
    return None

main()