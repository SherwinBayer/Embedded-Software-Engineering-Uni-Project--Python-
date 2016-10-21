import ProjectSetup as test
import RPi.GPIO as GPIO
import ProjectAdditionalComponents as test2

print(test.gpioList)
print(test.gpioInputList)

test.setup()
test2.addNewLED()

print(test.gpioList)
print(test.gpioInputList)

GPIO.cleanup()
