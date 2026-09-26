# Imports go at the top
from microbit import *


hat = Image("00000:"   
            "09990:"
            "99999:"
            "00000:"
            "00000")

speedos = Image("00000:"
                "00000:"  
                "99999:"
                "00900:"
                "00000")

while not button_b.was_pressed():
    if accelerometer.was_gesture("shake"):
        fahrenheit = temperature() * 9 / 5 + 32
        display.scroll(str(fahrenheit) + ".F")
    elif button_a.was_pressed():
        display.scroll(str(temperature()) + ".C")
    if temperature() < 21:
        display.scroll("Wear a jacket")
        display.show(Image.UMBRELLA)
    elif temperature() > 30:
        display.scroll("Break out the speedos")
        display.show(speedos)
    elif temperature() > 21:
        display.scroll("Wear a hat")
        display.show(hat)    
        sleep(1000)
display.scroll("STOPPED")        
    
        