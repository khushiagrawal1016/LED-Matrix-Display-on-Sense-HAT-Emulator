#Another way to display scrolling (running) text is given below:
from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 0)
yellow = (192, 192, 192)

while True:
  sense.show_message("SRM IST", text_colour=yellow, back_colour=blue, scroll_speed=0.2)
