# Description : Control LED with Photoresistor
from pathlib import Path
import sys
import time
import RPi.GPIO as GPIO

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

ledPins = [33, 40, 35, 15, 36, 16, 37, 18, 12,22]
ADC = ADCDevice() # Define an ADCDevice class object

def setup():
    global ADC
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(ledPins, GPIO.OUT)
        
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
    
def loop():
    global ADC
    global x
    while True:
        value = ADC.analogRead(0) # read the ADC value of channel 0
        voltage = value / 255
              
        for x in range(0,10):
            if value >= 255/10 * x:
                GPIO.output(ledPins[x], GPIO.LOW)   
            else:
                 GPIO.output(ledPins[x], GPIO.HIGH) 
                     
             
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} ')
        time.sleep(0.01)

def destroy():
    global ADC
    ADC.close()
    GPIO.cleanup() 
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        
