from gpiozero import LED as LEDClass
import subprocess

LED_Green = LEDClass(17)  # define ledPin
LED_Red = LEDClass(18)  # define buttonPin

def is_internet_connected():
    try:
        # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

def loop():
    global LED_Green
    global LED_Red
    while True:
        if is_internet_connected() == True: 
            LED_Red.off()
            LED_Green.on() 
            print ("green led turned on >>>") 
        else:  
            LED_Green.off() 
            print ("green led turned off <<<")
            LED_Red.on()
            print ("red led turned on >>>")
                

def destroy():
    global LED_Red
    global LED_Green
    # Release resources
    LED_Red.close()
    LED_Green.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
