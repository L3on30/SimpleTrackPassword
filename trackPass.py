from ntpath import join
import random
import pyautogui


char = "qwertyuiopasdfghjklzxcvbnm1234567890"
charlist = list(char)


password = pyautogui.password("Enter your password: ")

trackPassword = ""

while (trackPassword != password):
    trackPassword = random.choices(charlist, k = len(password))
    print("Tracking: " + str(trackPassword))
    if trackPassword == list(password):
        print("The password: " + "".join(trackPassword))
        break


