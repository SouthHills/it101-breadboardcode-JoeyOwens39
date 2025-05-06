from gpiozero import RGBLED, Button
import time
import random
from signal import pause

LED = RGBLED(red=5, green=13, blue=19, active_high=True)
BUTTON = Button(16)
colors = ([1,0,0],[0,1,0],[0,0,1])

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)
    
def set_color2():
    print("button pressed")
    LED.color = (1 - 1, 1 - 0, 1 - 0)
    

def loop():
    global BUTTON
    global LED
    global colors
    while True:
        random_color = random.randint(0,2)
        
        print(random_color)
        set_color(colors[random_color][0],colors[random_color][1],colors[random_color][2])
        time.sleep(1)
        if random_color == 1:
            
            if BUTTON.is_pressed:
                print("Button green pressed")
                for x in range(0,6):
                    LED.off()
                    time.sleep(1)
                    LED.on()
            time.sleep(10)
        else:
            if BUTTON.is_pressed:
                set_color(colors[0][0],colors[0][1],colors[0][2])
                for x in range(0,6):
                    LED.off()
                    time.sleep(1)
                    LED.on()
                
