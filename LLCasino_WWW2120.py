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
    print("LLCasino_WWW2120.py started. Press 'q' to quit.")
    while True:
        if keyboard.is_pressed('esc'):
            print("Quitting...")
            break
        
        t = 0.5
        l = 0.2
        T = time_noise(t, l)
        time.sleep(T)

        x, y = 1665, 959
        r = 10
        X, Y = circle_noise(x, y, r)
        pyautogui.moveTo(X, Y, duration=time_noise(0.2, 0.1))
        # Click with noise
        pyautogui.click()

    print("LLCasino_WWW2120.py ended.")
    return

main()