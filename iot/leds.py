# Name: Valentine Kimani
# Date: 26/02/2026
# program to display led


from machine import Pin
import time
import machine


red_led = Pin(28, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
#button input
green_btn =Pin(22, Pin.IN,Pin.PULL_UP)
while True:
    button_status = green_btn.value()
    if (button_status==1):
        red_led.off()
        print("Button released ")
    elif (button_status==0):
        red_led.on()
        print("Button pressed ")

    red_led.on()
    time.sleep(1)