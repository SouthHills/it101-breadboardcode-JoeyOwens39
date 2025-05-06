import subprocess
import time
from gpiozero import Button
from signal import pause
FIREFOX_BUTTON = Button(23)
CHROME_BUTTON = Button(21)
chrome_bool = False
firefox_bool = False


def open_firefox():
    global firefox_bool
    global FIREFOX_BUTTON
    firefox_bool = not firefox_bool
    if firefox_bool == True:
        global process_firefox 
        process_firefox = subprocess.Popen("firefox")   
    else:
        process_firefox.terminate()
                
def open_chrome():
    global chrome_bool
    global CHROME_BUTTON
    chrome_bool = not chrome_bool
    if chrome_bool == True:
        global process_chrome
        process_chrome = subprocess.Popen("chromium")   
    else:
        process_chrome.terminate()
    
def destroy():
    FIREFOX_BUTTON.close()
    CHROME_BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")

    try:
        # If the button gets pressed, call the function
        # This is an event
        FIREFOX_BUTTON.when_pressed = open_firefox
        CHROME_BUTTON.when_pressed = open_chrome
        pause()
        
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
