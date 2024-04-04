import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = [26, 16, 25, 24, 23, 17, 27, 22] # GPIO Pin Numbers
for light in led:
	GPIO.setup(light, GPIO.OUT)
fib=[0,1,1,2,3,5,8]

try:
	for i in fib:
		for light in range(i):
				print(f"LED {light} ON")
				GPIO.output(led[light], GPIO.HIGH)
		time.sleep(0.2)
		for light in range(i):
				print(f"LED {light} ON")
				GPIO.output(led[light], GPIO.LOW)
finally:
	for light in led:
		GPIO.output(light, GPIO.LOW)