import time
from neopixel import Neopixel

from text import TextString

# Define the GPIO pin
GPIO_PIN = 28

# Define the array size
nrows = 8
ncols = 32
numpix = nrows * ncols


# Define the colors


# for some reason does not run in RGB mode
def convert_RGB_to_GRB(tuple_rgb: tuple) -> tuple:
    """convert RGB tuple to GRB tuple"""
    return tuple_rgb[1], tuple_rgb[0], tuple_rgb[2]


# Define some colors
zero = (0, 0, 0)
r = convert_RGB_to_GRB((255, 0, 0))
g = convert_RGB_to_GRB((0, 255, 0))
b = convert_RGB_to_GRB((0, 0, 255))


# LEDWALL

# NOTE:
# the nativE pixel indexing starts at 0
# and zigzags from the input side (see back of the LED panel)
# to the output side


class LedWall(Neopixel):
    _default_brightness = 1

    def __init__(self, nrows, ncols, GPIO_PIN):
        self.nrows = nrows
        self.ncols = ncols
        self.numpix = nrows * ncols
        # create the neopixel object
        super().__init__(self.numpix, 0, GPIO_PIN, mode="RGB")
        self.brightness(self._default_brightness)

    def get_pixel_number(self, x, y):
        """get linar pixel number from x, y coordinates"""
        if x % 2 == 0:
            return x * self.nrows + y
        else:
            return x * self.nrows + (nrows - 1 - y)

    def exit(self):
        self.clear()
        self.show()


l = LedWall(nrows, ncols, GPIO_PIN)

while True:
    try:
        # demo(numpix, ledwall, zero, colors)
        TextString("CIAO", l).display(0, r)
        # print_word("CIAO", r, ledwall, zero)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
    except Exception as e:
        print(e)
        break
# exit
l.exit()
print("Finished.")
