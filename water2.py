import RPi.GPIO as GPIO
import smtplib 
import time, datetime
#import BlynkLib
#BLYNK_AUTH='xVvbrE_KjotlxB50aAWgRF7XwW5zs417'
#blynk=BlynkLib.Blynk(BLYNK_AUTH)

import time, sys
pulse_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulse_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
global count 
count=0
flag=0
print('Enter the calibration constant')
x=float(input())
print('Enter the limit in litres')
limit=float(input())
def countPulse1(channel):
        global count
        count=count+1
        
        print(1, end='')

GPIO.add_event_detect(pulse_pin, GPIO.RISING, callback=countPulse1)

try:
        while flag==0:
                print('Initializing')
                time.sleep(10)
                flag+=1
                
                
except KeyboardInterrupt:
        print ('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        sys.exit()

val=count
print('\n**************************')
print('Water Used = %.2f litres' % (float(val)*x))
print('**************************')
#@blynk.on("V3")

#def v3_write_handler(value):
 #       print('Calibrating value',value[0])
      
#while True:
 #       blynk.run()        
GPIO.cleanup()
ans=round((float(val)*x),3)
if(ans>=limit):
        over=ans-limit
        rem=0
else:
        over=0
        rem=limit-ans 
rem=round(rem,3)
over=round(over,3)
email = 'pulkit.thapar2018@vitstudent.ac.in'
password = 'methapar'
send_to_email = 'pulkit.thapar2018@vitstudent.ac.in' 
message = 'Volume of water consumed = ' + str(ans) + ' litres'+'\n'+'Remaining = '+str(rem)+' litres '+'\n'+'Overhead = '+str(over)+' litres '+'\n\n\n'+'[Sent from Rasberry Pi]'


server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
print('Sending email...\n')
server.sendmail(email, send_to_email , message) # Send the email
server.quit() # Logout of the email server
print('Done')
