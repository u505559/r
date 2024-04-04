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
