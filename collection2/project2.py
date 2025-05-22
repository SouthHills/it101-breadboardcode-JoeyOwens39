from pathlib import Path
from gpiozero import LED as LEDClass
import sys
import time
LED_Blue = LEDClass(13)
LED_Green = LEDClass(26)
LED_Yellow = LEDClass(19)
LED_Red = LEDClass(5)


HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False 

ADC = ADCDevice() 

def setup():
    global ADC
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
    global ADC, LED_Blue, LED_Green, LED_Yellow, LED_Red
    while True:
        value = ADC.analogRead(0)    # read the ADC value of channel 0
        voltage = value / 255.0 * 3.3  # calculate the voltage value
        print(f'ADC Value: {value} \tVoltage: {voltage:.2f}')
        time.sleep(0.1)
        if value > 0 and value < 63:
            LED_Blue.on()
            LED_Green.off()
            LED_Yellow.off()
            LED_Red.off()
        elif value > 63 and value < 126:
            LED_Blue.on()
            LED_Green.on()
            LED_Yellow.off()
            LED_Red.off()
        elif value > 126 and value < 189:
            LED_Blue.on()
            LED_Green.on()
            LED_Yellow.on()
            LED_Red.off()
            
        elif value > 189 and value < 241:
            LED_Blue.on()
            LED_Green.on()
            LED_Yellow.on()
            LED_Red.off()
            
        elif value > 241 and value < 255:
            LED_Blue.on()
            LED_Green.on()
            LED_Yellow.on()
            LED_Red.on()           
            
        else:
            LED_Blue.off()
            LED_Green.off()
            LED_Yellow.off()
            LED_Red.off()
        
def destroy():
    global ADC, LED_Blue, LED_Green, LED_Yellow, LED_Red 
    ADC.close()
    LED_Blue.close()
    LED_Green.close()
    LED_Yellow.close()
    LED_Red.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()   