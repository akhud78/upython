"""CircuitPython simple NeoPixel example"""
import time
import board
import neopixel_write
import digitalio

YELLOW = (150, 150, 0)

def rgb_blink(number=5, color=YELLOW):
    """RGB LED blinking
    
    ```python
    GREEN = (255, 0, 0)
    YELLOW = (150, 150, 0)
    RED = (0, 255, 0)
    BLUE = (0, 0, 255)
    ```
    :param number: number of flashes
    :type number: int
    :param color: RGB LED color
    :type color: tuple
    """
    pin = digitalio.DigitalInOut(board.NEOPIXEL)
    pin.direction = digitalio.Direction.OUTPUT
    led_off = bytearray([0, 0, 0])  
    led_on = bytearray(color)  # grb

    for _ in range(number):
        neopixel_write.neopixel_write(pin, led_on)
        time.sleep(0.2)
        neopixel_write.neopixel_write(pin, led_off)
        time.sleep(0.2)

if __name__ == '__main__':
    rgb_blink()