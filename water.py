import RPi.GPIO as GPIO
import time,sys
GPIO.setmode(GPIO.BOARD)
inpt=16
GPIO.setup(inpt,GPIO.IN)
cal=float(input())
rate_cnt=0
tot_cnt=0
minutes=0
constant=1.00/cal
time_new=0.0

print('Approx water flow')

while True:
	time_new=time.time()+10
	rate_cnt=0
	while True:
		if GPIO.input(inpt)==1:
			rate_cnt+=1
			tot_cnt+=1
		try:
			print(GPIO.input(inpt), end='')
			time.sleep(1)
		except KeyboardInterrupt:
			print('\n Exiting')
			GPIO.cleanup()
			sys.exit()
	minutes+=1
	print('/nLitres/min',rate_cnt*constant,4)
	print('Total Litres', round(tot_cnt*constant,4))
	print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime(time.time())),'\n')

GPIO.cleanup()
print('DONE')
