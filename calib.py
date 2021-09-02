import RPi.GPIO as GPIO
#import BlynkLib
#BLYNK_AUTH='xVvbrE_KjotlxB50aAWgRF7XwW5zs417'
#blynk=BlynkLib.Blynk(BLYNK_AUTH)

import time, sys
pulse_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulse_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
global count 
count=0
x=0
def countPulse1(channel):
        global count
        count=count+1
        print("Number of rotations of wheel of flow sensor:")
        print(count)

GPIO.add_event_detect(pulse_pin, GPIO.RISING, callback=countPulse1)

try:
        while x==0:
                print("Starting")
                time.sleep(10)
                print("Ending")
                x=x+1
                
except KeyboardInterrupt:
        print ('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        sys.exit()

constant=count
print('**************************')
print('One Litre = %.d rotations ' % constant)
print('Calibration constant= %.5f' %(1/constant))
print('**************************')
#@blynk.on("V3")

#def v3_write_handler(value):
 #       print('Calibrating value',value[0])
        
#while True:
 #       blynk.run()        
