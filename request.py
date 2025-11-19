from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
import os
import json
import time
import pyautogui
import keyboard

filename = "savepos.json"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        json.dump({
            "saved_position_Group": None,
            "saved_position_Share": None,
            "saved_position_Post": None,
            "saved_position_RateLimited": None
        }, f, indent=4)

with open(filename, "r") as f:
    savepos = json.load(f)

Post_To_Share = "https://www.facebook.com/share/p/16bQW5zGHL/?mibextid=wwXIfr"
Amount_Of_Groups = 45

driver = webdriver.Chrome()


def clickGroup():
    pyautogui.moveTo(savepos["saved_position_Group"][0], savepos["saved_position_Group"][1], duration=0.5)
    time.sleep(2)
    pyautogui.click()


def clickShare():
    pyautogui.moveTo(savepos["saved_position_Share"][0], savepos["saved_position_Share"][1], duration=0.5)
    time.sleep(2)
    pyautogui.click()


def clickPost():
    pyautogui.moveTo(savepos["saved_position_Post"][0], savepos["saved_position_Post"][1], duration=0.5)
    time.sleep(2)
    pyautogui.click()


def clsProgress(a):
    os.system('cls')
    print(f"[PROGRESS] Progress: {a - 1}/{Amount_Of_Groups} Groups.")
    print(f"[ATTEMPT] Attempting: Group {a} rightnow.")
    print("\n")


def clickLimitPost():
    pyautogui.moveTo(savepos["saved_position_RateLimited"][0], savepos["saved_position_RateLimited"][1], duration=0.5)
    time.sleep(2)
    pyautogui.click()


def main():
    global savepos

    print("[SYSTEM] Navigating...")

    for amount in range(1, Amount_Of_Groups + 1):
        Retry_Attempt = -1
        clsProgress(amount)

        driver.get("https://facebook.com")
        time.sleep(3)

        driver.get(Post_To_Share)
        time.sleep(5)

        if savepos["saved_position_Share"] is None:
            print("[SYSTEM] Move your cursor to the 'Share' Button and press 'X' to complete setup")

        while savepos["saved_position_Share"] is None:
            if keyboard.is_pressed('x'):
                savepos["saved_position_Share"] = list(pyautogui.position())
                pyautogui.hotkey('alt', 'tab')
                confirm_input = input("[INPUT] Confirm Position? Press [Y/N]: ")
                if confirm_input.upper() != "Y":
                    savepos["saved_position_Share"] = None
                else:
                    with open(filename, "w") as f:
                        json.dump(savepos, f, indent=4)

        clickShare()
        time.sleep(5)
        clsProgress(amount)

        if savepos["saved_position_Group"] is None:
            print("[SYSTEM] Move your cursor to the 'Group' Button and press 'X' to complete setup")

        while savepos["saved_position_Group"] is None:
            if keyboard.is_pressed('x'):
                savepos["saved_position_Group"] = list(pyautogui.position())
                pyautogui.hotkey('alt', 'tab')
                confirm_input = input("[INPUT] Confirm Position? Press [Y/N]: ")
                pyautogui.hotkey('alt', 'tab')

                if confirm_input.upper() != "Y":
                    savepos["saved_position_Group"] = None
                else:
                    with open(filename, "w") as f:
                        json.dump(savepos, f, indent=4)

        clsProgress(amount)
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

        if savepos["saved_position_Post"] is None:
            print("[SYSTEM] Move your cursor to the 'Post' Button and press 'X' to complete setup")

        while savepos["saved_position_Post"] is None:
            if keyboard.is_pressed('x'):
                savepos["saved_position_Post"] = list(pyautogui.position())
                pyautogui.hotkey('alt', 'tab')
                confirm_input = input("[INPUT] Confirm Position? Press [Y/N]: ")
                if confirm_input.upper() != "Y":
                    savepos["saved_position_Post"] = None
                else:
                    with open(filename, "w") as f:
                        json.dump(savepos, f, indent=4)

        clickPost()
        time.sleep(5)

        while True:
            try:
                element = driver.find_element(By.XPATH, "//div[contains(text(), 'We limit how often you can post')]")
                Retry_Attempt = Retry_Attempt + 1
                if savepos["saved_position_RateLimited"] is None:
                    print("[SYSTEM] Ratelimited Post Position NOT DETECTED!")
                    print("[SYSTEM] Move your cursor to the 'Post' Button and press 'X' to complete setup")
                    while savepos["saved_position_RateLimited"] is None:
                        if keyboard.is_pressed('x'):
                            savepos["saved_position_RateLimited"] = list(pyautogui.position())
                            pyautogui.hotkey('alt', 'tab')
                            confirm_input = input("[INPUT] Confirm Position? Press [Y/N]: ")
                            if confirm_input.upper() != "Y":
                                savepos["saved_position_RateLimited"] = None
                            else:
                                with open(filename, "w") as f:
                                    json.dump(savepos, f, indent=4)
                clsProgress(amount)
                now = datetime.now()
                future_time = now + timedelta(minutes=10)
                print(f"[SYSTEM] Retry Attempt: {Retry_Attempt}")
                print("[TASK] RateLimit Detected!, Retrying in 10 minutes @ ", future_time.strftime("%H:%M:%S"))
                time.sleep(600)
                clickLimitPost()

            except NoSuchElementException:
                print("[TASK] Shared Successfully!")
                break

        time.sleep(10)


os.system('cls')
driver.get("https://www.facebook.com")

input("[INPUT] Press enter after logging in.")
pyautogui.hotkey('alt', 'tab')

os.system('cls')
while True:
    main()

time.sleep(10000)
driver.quit()
