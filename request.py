from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time
import pyautogui
import keyboard

Post_To_Share = "https://www.facebook.com/share/p/16bQW5zGHL/?mibextid=wwXIfr"
Amount_Of_Groups = 10

driver = webdriver.Chrome()

saved_position_Group = None
saved_position_Share = None
saved_position_Post = None

def clickGroup():
    pyautogui.moveTo(saved_position_Group[0], saved_position_Group[1], duration=0.5)
    pyautogui.click()

def clickShare():
    pyautogui.moveTo(saved_position_Share[0], saved_position_Share[1], duration=0.5)
    pyautogui.click()

def clickPost():
    pyautogui.moveTo(saved_position_Post[0], saved_position_Post[1], duration=0.5)
    pyautogui.click()

def main():
    global saved_position_Share
    global saved_position_Group
    global saved_position_Post

    print("Navigating...")

    for amount in range(1, Amount_Of_Groups + 1):
        print(f"{amount} Groups")

        driver.get("https://facebook.com")
        time.sleep(3)

        driver.get(Post_To_Share)
        time.sleep(5)

        if saved_position_Share is None:
            print("Move your cursor to the 'Share' Button and press 'X' to complete setup")

        while saved_position_Share is None:
            if keyboard.is_pressed('x'):
                saved_position_Share = pyautogui.position()
                pyautogui.hotkey('alt', 'tab')
                confirm_input = input("Confirm Position? Press [Y/N]: ")
                if confirm_input.upper() != "Y":
                    saved_position_Share = None

        clickShare()
        time.sleep(5)
        os.system('cls')

        if saved_position_Group is None:
            print("Move your cursor to the 'Group Button' and press 'X' to complete setup")

        while saved_position_Group is None:
            if keyboard.is_pressed('x'):
                saved_position_Group = pyautogui.position()
                pyautogui.hotkey('alt', 'tab')
                confirm_input = input("Confirm Position? Press [Y/N] ")
                pyautogui.hotkey('alt', 'tab')

                if confirm_input.upper() == "Y":
                    print(f"Position saved at: {saved_position_Group}")
                    time.sleep(1)
                else:
                    saved_position_Group = None

        clickGroup()
        time.sleep(5)

        for i in range(1, 4):
            time.sleep(0.1)
            pyautogui.keyDown('tab')

        extraclick = (amount - 1) * 2
        if extraclick > 0:
            for i in range(1, extraclick + 1):
                time.sleep(0.1)
                pyautogui.keyDown('tab')

        time.sleep(1)
        pyautogui.keyDown('enter')
        time.sleep(10)

        if saved_position_Post is None:
            print("Move your cursor to the 'Post' Button and press 'X' to complete setup")

        while saved_position_Post is None:
            if keyboard.is_pressed('x'):
                saved_position_Post = pyautogui.position()
                pyautogui.hotkey('alt', 'tab')
                confirm_input = input("Confirm Position? Press [Y/N]: ")
                if confirm_input.upper() != "Y":
                    saved_position_Post = None

        clickPost()

        time.sleep(1)
        pyautogui.keyDown('enter')
        print("Shared Successfully!")
        time.sleep(10)

os.system('cls')
driver.get("https://www.facebook.com")
os.system('cls')

input("Press enter after logging in.")
pyautogui.hotkey('alt', 'tab')

os.system('cls')

while True:
    main()

time.sleep(10000)
driver.quit()



