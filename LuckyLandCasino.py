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

GRAY_COLORS = [
    (155, 161, 165),
    (175, 180, 183),
    (184, 188, 191),
    (193, 197, 200),
    (203, 206, 208),
    (216, 219, 220),
    (227, 229, 230),
    (235, 236, 237),
    (243, 244, 244),
    (247, 248, 248),
    (252, 253, 253),
    (254, 255, 255),
    (255, 255, 255),
    (248, 249, 249),
    (238, 239, 240),
    (231, 232, 233),
    (224, 226, 228),
    (212, 215, 216),
    (189, 193, 196),
    (180, 184, 188),
    (163, 169, 173),
    (152, 158, 162),
    (142, 149, 153),
    (132, 139, 144),
    (130, 137, 142),
    (131, 138, 143),
    (133, 140, 145),
    (136, 143, 148),
    (145, 150, 155),
    (151, 157, 162),
    (169, 175, 179),
    (178, 183, 186),
    (196, 200, 203),
    (206, 209, 211),
    (214, 217, 218),
    (223, 225, 227),
    (239, 240, 241),
    (245, 246, 246),
    (249, 250, 250),
    (253, 254, 254),
    (250, 251, 251),
    (242, 243, 243),
    (232, 233, 234),
    (205, 208, 210),
    (186, 190, 193),
    (177, 182, 185),
    (153, 159, 164),
    (148, 154, 158),
    (137, 144, 149),
    (138, 145, 150),
    (150, 156, 160),
    (157, 163, 167),
    (165, 171, 175),
    (174, 179, 182),
    (187, 191, 194),
    (209, 212, 214),
    (222, 224, 226),
    (230, 231, 232),
    (244, 245, 245),
    (240, 241, 242),
    (233, 234, 235),
    (219, 221, 223),
    (201, 204, 206),
    (183, 188, 190),
    (158, 164, 168),
    (143, 150, 154),
    (139, 146, 151),
    (135, 142, 147),
    (149, 155, 159),
    (171, 176, 179),
    (199, 203, 205),
    (208, 211, 213),
    (241, 242, 243),
    (228, 229, 230),
    (220, 222, 224),
    (198, 202, 204),
    (180, 185, 188),
    (152, 158, 163),
    (147, 153, 157),
    (141, 148, 152),
    (134, 141, 146),
    (144, 150, 154),
    (159, 165, 169),
    (167, 173, 177),
    (188, 192, 195),
    (215, 218, 219),
    (251, 252, 252),
    (246, 247, 247),
    (221, 223, 225),
    (204, 207, 209),
    (195, 199, 202),
    (168, 174, 178),
    (160, 166, 170),
    (140, 147, 152),
    (145, 151, 155),
    (161, 167, 171),
    (218, 221, 222),
    (237, 238, 239),
    (226, 228, 230),
    (141, 148, 153),
    (176, 181, 184),
    (185, 189, 192),
    (183, 188, 191),
    (171, 176, 180),
    (162, 168, 172),
    (130, 137, 143),
    (144, 150, 155),
    (155, 161, 166),
    (166, 172, 176),
    (212, 215, 217),
    (217, 220, 221),
    (207, 210, 212),
    (197, 201, 204),
    (146, 152, 156),
    (156, 162, 167),
    (186, 190, 194),
    (210, 213, 215),
    (178, 182, 186),
    (150, 155, 160),
    (143, 149, 154),
    (138, 144, 149),
    (137, 144, 148),
    (156, 162, 166),
    (236, 237, 238),
    (224, 226, 227),
    (211, 214, 215),
    (183, 187, 190),
    (149, 154, 159),
    (144, 149, 154),
    (139, 146, 150),
    (167, 173, 176),
    (225, 227, 228),
    (179, 184, 187),
    (197, 201, 203),
    (190, 194, 197),
    (172, 177, 180),
    (154, 160, 164),
    (211, 214, 216),
    (229, 230, 231),
    (213, 216, 217),
    (168, 174, 177),
    (153, 159, 163),
    (140, 147, 151),
    (169, 175, 178),
    (147, 152, 157),
    (217, 219, 221),
    (191, 195, 198),
    (154, 160, 165),
    (148, 153, 158),
    (150, 156, 161),
    (164, 170, 174),
    (181, 186, 189),
    (200, 203, 205),
    (192, 196, 199),
    (138, 145, 149),
    (225, 227, 229),
    (173, 178, 181),
    (170, 176, 179),
    (234, 235, 236),
    (194, 198, 201),
    (143, 150, 155),
    (158, 164, 169)
]

COLORS = [
    (91, 56, 124),
    (91, 55, 123),
    (92, 55, 122),
    (92, 56, 120),
    (93, 57, 121),
    (94, 58, 122),
    (95, 59, 123),
    (95, 59, 124),
    (95, 58, 125),
    (96, 60, 124),
    (97, 61, 125),
    (91, 56, 122),
    (92, 56, 121),
    (95, 58, 124),
    (91, 56, 123),
    (92, 55, 121),
    (95, 59, 121),
    (96, 60, 122),
    (96, 60, 123),
    (97, 61, 123),
    (95, 59, 122),
    (90, 55, 123),
    (91, 55, 122),
    (91, 55, 121),
    (96, 59, 123),
    (96, 59, 125),
    (96, 59, 124),
    (96, 59, 126),
    (97, 61, 124),
    (91, 56, 121),
    (96, 59, 122),
    (93, 56, 121),
    (93, 57, 122),
    (94, 58, 123),
    (93, 56, 123),
    (94, 57, 124),
    (93, 57, 123),
    (94, 58, 121),
    (94, 57, 123),
    (94, 58, 120),
    (93, 56, 122),
    (96, 58, 125),
]

COLLECT_COLORS = [
    (249, 189, 250),
    (249, 189, 249),
    (249, 189, 248),
    (251, 189, 251),
    (250, 189, 251),
    (250, 189, 250),
    (249, 189, 251),
    (250, 188, 250),
    (248, 189, 250),
    (249, 189, 252),
    (251, 188, 250),
    (250, 188, 251),
    (248, 189, 251),
    (253, 190, 252),
    (251, 191, 252),
    (251, 191, 251),
    (251, 191, 250),
    (252, 190, 252),
    (252, 190, 251),
    (251, 190, 251),
    (251, 190, 250),
    (252, 189, 252),
    (252, 189, 251),
    (250, 190, 250),
    (250, 190, 249),
    (248, 191, 249),
    (251, 189, 250),
    (249, 190, 250),
    (250, 189, 249),
    (248, 189, 252),
    (247, 189, 252),
    (248, 189, 249),
    (248, 189, 248),
    (253, 190, 251),
    (253, 190, 250),
    (252, 190, 250),
    (251, 188, 249),
    (250, 188, 249),
    (250, 190, 252),
    (250, 190, 251),
    (249, 190, 252),
    (249, 190, 251),
    (250, 189, 252),
    (248, 190, 252),
    (248, 190, 251),
    (247, 189, 250),
    (249, 188, 250),
    (248, 188, 250),
    (250, 188, 252),
    (251, 188, 252),
    (249, 188, 252),
    (250, 189, 248),
    (251, 188, 248),
    (250, 188, 248),
    (247, 189, 249),
    (249, 188, 248),
    (247, 189, 248),
    (248, 190, 249),
    (249, 188, 249),
    (248, 188, 249),
    (251, 190, 252),
    (252, 190, 249),
    (252, 190, 248),
    (252, 190, 247),
    (251, 190, 249),
    (251, 191, 253),
    (250, 189, 253),
    (253, 188, 250),
    (252, 188, 252),
    (252, 188, 251),
    (254, 187, 250),
    (252, 188, 250),
    (253, 187, 251),
    (251, 188, 251),
    (253, 187, 250),
    (249, 189, 253),
    (248, 189, 253),
    (249, 188, 251),
]

def get_back_to_game():
    bIsBackToGame = True

    nCount = 0
    while True:
        bBreakLoop = False
        try:
            # click on game
            location = pyautogui.locateOnScreen("Images/RECONNECT.png",region=(740, 667, 1179, 823), confidence=0.9)

            if location is not None:
                print(f"Success! Found at {location}...")
                nCount += 1
                pyautogui.click(961, 748)
                time.sleep(2)
                bIsBackToGame = False
            else:
                print("Image not currently on screen.")
                bBreakLoop = True
            
            if nCount >= 5:
                pyautogui.click(132, 63) # need to refresh browser
                time.sleep(10)
                bBreakLoop = True
        except pyautogui.ImageNotFoundException:
            # print("Error: PyAutoGUI specifically couldn't find the image.")
            bBreakLoop = True
            pass
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            bBreakLoop = True
        if bBreakLoop:
            break


    cPURPLE = get_pixel_color(959, 943)
    if (cPURPLE in COLORS):
        pyautogui.click(1625, 849)
        time.sleep(10)
        bIsBackToGame = False

    cRESET = get_pixel_color(756, 363)
    if (cRESET == (255, 255, 255)):
        time.sleep(0.1)
        cReset2 = get_pixel_color(756, 363)
        if (cReset2 == (255, 255, 255)):
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1203, 998)
            time.sleep(0.1)
            pyautogui.click(1490, 999)
            time.sleep(0.5)
            pyautogui.click(1487, 912)
            time.sleep(0.5)
            pyautogui.click(1651, 965)
            time.sleep(5)
            bIsBackToGame = False

    cSTOP = get_pixel_color(1650, 988)
    if (cSTOP != (255, 255, 255)):
        bIsBackToGame = False
        cSTOP2 = get_pixel_color(1620, 985)
        if (cSTOP2 in GRAY_COLORS):
            pyautogui.click(1650, 988)
            time.sleep(0.1)


    cCOLLECT = get_pixel_color(825, 467)
    if (cCOLLECT in COLLECT_COLORS):
        time.sleep(0.1)
        cCOLLECT2 = get_pixel_color(825, 467)
        if (cCOLLECT2 in COLLECT_COLORS):
            print("Collecting reward...")
            pyautogui.click(959, 469)
            time.sleep(5)
            bIsBackToGame = False

    try:
        # exit button
        location = pyautogui.locateOnScreen("Images/Exit1.png",region=(176, 123, 1836, 336), confidence=0.9)

        if location is not None:
            print(f"Success! Found at {location}...")
            pyautogui.click(location)
            time.sleep(5)
            bIsBackToGame = False

        else:
            print("Image not currently on screen.")
    except pyautogui.ImageNotFoundException:
        pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    try:
        # enter search for game
        location = pyautogui.locateOnScreen("Images/EnterSearch.png",region=(176, 123, 1836, 336), confidence=0.9)

        if location is not None:
            print(f"Success! Found at {location}...")
            pyautogui.click(1495, 259)
            pyautogui.typewrite("star")
            time.sleep(5)
            bIsBackToGame = False

        else:
            print("Image not currently on screen.")
    except pyautogui.ImageNotFoundException:
        # print("Error: PyAutoGUI specifically couldn't find the image.")
        pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        # click on game
        location = pyautogui.locateOnScreen("Images/StarSpell.png",region=(406, 309, 719, 510), confidence=0.9)

        if location is not None:
            print(f"Success! Found at {location}...")
            pyautogui.click(location)
            time.sleep(5)
            bIsBackToGame = False

        else:
            print("Image not currently on screen.")
    except pyautogui.ImageNotFoundException:
        # print("Error: PyAutoGUI specifically couldn't find the image.")
        pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

    # reconnection buttons
    delay = 0.5
    L = 0.1
    t = time_noise(delay, L)
    pyautogui.click(974, 698)
    time.sleep(t)
    pyautogui.click(714, 911)
    time.sleep(t)

    return bIsBackToGame

def main():
    # click coords
    xc, yc = 958, 697
    R = 6

    delay = 0.5
    L = 0.1

    print("starting...")
    while True:

        bExit = False
        while True:
            bIsBackToGame = get_back_to_game()
            if bIsBackToGame:
                break
            
            if keyboard.is_pressed('esc'):
                print("Stopping...")
                bExit = True
                break
        if bExit:
            break

        t = time_noise(delay, L)
        
        if True:
            # time.sleep(t+0.1)
            XC, YC = circle_noise(xc, yc, R)
            time.sleep(t)
            pyautogui.click(XC, YC)
            print("clicking mouse...")


        

        
        if keyboard.is_pressed('esc'):
            print("Stopping...")
            break
    return

main()


# 2:12      24->25
# 11:48:06  35->36

