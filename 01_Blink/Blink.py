from gpiozero import LED as LEDClass # Alias
import time

LED = LEDClass(17)  # define led
LED2 = LEDClass(18)

def loop():
    global LED
    while True:
        LED.on() 
        print ("led turned on >>>") # print information on terminal
        time.sleep(1)
        LED.off()
        print ("led turned off <<<")
        LED2.on()
        print ("led2 turned on >>>")
        time.sleep(1)
        LED2.off()
        
def destroy():
    global LED
    # Release resources
    LED.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pin {LED.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
