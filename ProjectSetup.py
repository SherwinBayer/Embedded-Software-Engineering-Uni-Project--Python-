import RPi.GPIO as GPIO

gpioList = [5,6,13,19,26] #GPIO pins that will operate the LED's as output,
#(for the demo, 5 and 6 are the kitchen lights, 13, 19 and 26 - bedroom lights)

gpioInputList = [21,20,16,12,25] #GPIO pins that will read the data from the
#buttons, these will be configured as input, each pin will correspond to the
#LED output pins in gpioList based on their index in the list
#(for the demo, 21 and 20 are the buttons associated with the kitchen lights,
#16, 12 and 25 - buttons associated with the bedroom lights)

#CONNECT THE WIRES TO THE PI's HEADER PINS ACCORDINGLY!

lightStatesList = [] #This list will hold the current states of the LED's
gpioPinsAvail = [17,27,22,18,23] #Available GPIO pins left unconfigured
#when the program is first run, GPIO pin 24 will be allocated the button
#for calling addNewLED()

#This function will be used to setup the pins for input and output
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for pin in gpioList:
        GPIO.setup(pin,GPIO.OUT)

    for pin in gpioInputList:
        GPIO.setup(pin,GPIO.IN)

