# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

inPin = 14
preIn = 0
count = 0


def setupGpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(inPin, GPIO.IN)


def main():
    global count
    curIn = GPIO.input(inPin)
    if(preIn == 1):
        if(GPIO.input(inPin) == 0):
            print("OFF")
    else:
        if(GPIO.input(inPin) == 1):
            print("ON")
            count += 1
            print("ボタンは{}回押されました".format(count))
    global preIn
    preIn = curIn


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    setupGpio()
    while True:
        try:
            main()
            time.sleep(0.2)
        except KeyboardInterrupt:
            destroy()
