from gpiozero import LED as LEDClass, Button
from signal import pause

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin

button_on = False
def changeLedState():
    global LED
    global button_on
    button_on = not button_on
    if button_on == True:
        print ("led turned on >>>")
        LED.blink()
    elif button_on == False:
        print ("led turned off <<<")
        LED.off()

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")

    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = changeLedState
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
    
