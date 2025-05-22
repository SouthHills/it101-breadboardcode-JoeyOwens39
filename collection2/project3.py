from gpiozero import RGBLED
import time
import random
from pathlib import Path

path = Path('/sys/class/thermal/thermal_zone0/temp')
LED = RGBLED(red=17, green=18, blue=27, active_high=True)

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)
    
    
def loop():
    while True :
        contents = path.read_text()
        contents = int(contents)
        cpu_temp = contents / 1000
        print(cpu_temp)
        
        if cpu_temp <= 15:
            set_color(0, 0, 1)
        elif cpu_temp >= 80:
            set_color(1, 0, 0)
        else:
            
    
        # time.sleep(.0001)

        
def destroy():
    LED.close()
    
if __name__ == '__main__':     
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()