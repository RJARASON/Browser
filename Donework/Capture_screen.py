try:
    import pyscreenshot as ImageGrab
    import os

    os.system("cls")
    screenshot=ImageGrab.grab()
    screenshot.save('C:/Users/MESSIE/Pictures/Screenshots/screenshot.png')
    print("Screenshot saved!")
    screenshot.show()
except Exception:
    os.system("cls")
    print("An error occured.")