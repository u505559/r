"""led module

GPIO(26) : 37 pin
GPIO(16) : 36
GPIO(25) : 22
GPIO(24) : 18
GPIO(23) : 16
GPIO(17) : 11
GPIO(27) : 13
GPIO(22) : 15"""






#fibo
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







#led
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = [26, 16, 25, 24, 23, 17, 27, 22] # GPIO Pin Numbers
for light in led:
	GPIO.setup(light, GPIO.OUT)
try:
	while True:
		for light in led:
				print(f"LED {light} ON")
				GPIO.output(light, GPIO.HIGH)
				time.sleep(0.02)
				print(f"LED {light} OFF")
				GPIO.output(light, GPIO.LOW)
				time.sleep(0.02)
finally:
	for light in led:
		GPIO.output(light, GPIO.LOW)







#emoji
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep
smiley = [
    "00111100",
    "01000010",
    "10100101",
    "10000001",
    "10011001",
    "10100101",
    "01000010",
    "00111100"
    ]
def draw_smiley(draw):
    for y in range(8):
        for x in range(8):
            if smiley[y][x] == "1":
                draw.point((x, y), fill="white")
# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
# Display the smiley emoji
with canvas(device) as draw:
    draw_smiley(draw)
# Wait for 5 seconds
sleep(45)
# Clear the LED matrix
device.clear()








#horizontal
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT
message = "Hello, Raspberry Pi!"
scroll_delay=0.3
def draw_message(draw,position):
    text(draw, (position,0), message, fill="white", font=proportional(CP437_FONT))
# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
#message width
message_width=len(message)*8
# Display the message
for i in range(message_width):
    with canvas(device) as draw:
        draw_message(draw,-i)
    sleep(scroll_delay)
# Clear the LED matrix
device.clear()