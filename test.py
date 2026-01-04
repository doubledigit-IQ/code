from PIL import ImageGrab

def get_pixel_color(x, y):
    # Take screenshot of the entire screen
    img = ImageGrab.grab()
    # Get RGB at (x, y)
    return img.getpixel((x, y))

x, y = 1613, 951

X = []
for i in range(1000):
    color = get_pixel_color(x, y)
    if color not in X:
        X.append(color)
        print(color)

