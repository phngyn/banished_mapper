import time
import pyautogui
import pydirectinput

def screen_bot():

# Steps:
# Check if on home screen
#   if yes, click new <Button y: 570+20, x: 1650+145>
#       in new, take screenshot <full y: 505+360, x: 1490+455> ; <Seed, type, size: y: 585+80, x: 1660+100>
#       click OK <Button y: 835+15, x: 1850+80>
#       wait until game loads
#       when game loads:
#           click gear, minimap (send keys if easier)
#           take screenshot
#           Go to menu
#           Exit
#           Wait until we're in home screen <y: 830+20, x: 1655+145>



    return None

def click_newgame():
    # ok_button = './marks/ok.jpg'
    # ok_loc = pyautogui.locateCenterOnScreen(ok_button)
    # print(ok_loc)
    pydirectinput.click(x=1650+25, y=570+30, clicks=2, interval=1, button='left')
    pyautogui.press('p')

def click_ok_newgame():
    # ok_button = './marks/ok.jpg'
    # ok_loc = pyautogui.locateCenterOnScreen(ok_button)
    # print(ok_loc)
    #  
    pydirectinput.click(x=1850+25, y=835+30, clicks=2, interval=1, button='left')
    pyautogui.press('p')

if __name__ == '__main__':

    # time.sleep(2)
    click_newgame()

    # time.sleep(2)    
    click_ok_newgame()
