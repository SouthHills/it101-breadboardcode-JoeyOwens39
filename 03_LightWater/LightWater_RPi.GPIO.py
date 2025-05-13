# Due to using special pins, the higher abstracted GPIOZero library cannot be used.
# The RPi.GPIO library can be used instead.
import RPi.GPIO as GPIO
import time

ledPins = [33, 40, 35, 15, 36, 16, 37, 18, 12,22]

def setup():    
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT)   # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led

def loop():
    while True:
        for pin in ledPins:     # make led(on) move from left to right
            GPIO.output(pin, GPIO.LOW)  
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        for pin in ledPins[::-1]:       # make led(on) move from right to left
            GPIO.output(pin, GPIO.LOW)  
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)

def destroy():
    GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

