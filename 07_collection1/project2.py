import time
from gpiozero import LED as LEDClass

LED_RED = LEDClass(18)
LED_YELLOW = LEDClass(17)
LED_GREEN = LEDClass(25)

def simulator():
    while True:
        LED_RED.on()
        time.sleep(5)
        LED_RED.off()
        LED_GREEN.on()
        time.sleep(7)
        LED_GREEN.off()
        LED_YELLOW.on()
        time.sleep(2)
        LED_YELLOW.off()
        
def destroy():
    LED_YELLOW.close()
    LED_GREEN.close()
    LED_RED.close()
    
    
if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")

    try:
        # If the button gets pressed, call the function
        # This is an event
        simulator()
        
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()