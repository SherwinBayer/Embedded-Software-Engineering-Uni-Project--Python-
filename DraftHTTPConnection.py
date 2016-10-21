import http.client as http
from pprint import pprint
import json
import RPi.GPIO as GPIO
import time

piNo = 1
gpioList = [5,6,13,19,26] #GPIO pins to be setup for output
lightStatesList = []
gpioInputList = [21]
'''gpioList = [ #Old GPIO pins for output
    18,
    23,
    24,
    17,
    27
]'''

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in gpioList:
    GPIO.setup(pin,GPIO.OUT)

for pin in gpioInputList:
    GPIO.setup(pin,GPIO.IN)

#FUNCTION Get State Update - Call every 1s
#URL to be /GPIOStates    
conn = http.HTTPConnection("pi-home-appliances.herokuapp.com")
conn.request("GET", "/GPIOStatuses", None, {"rpino":1}) #/notes, header={"PiNo:PiNo"}
response = conn.getresponse()

print(response.status)
print(response.version)
print(response.reason)

#body = response.read()
#conn.close()

if (response.status >= 200) & (response.status < 300):
    body = response.read()
    print("GET REQUEST 1")
    print(body)
    #conn.close()
    #Maybe send a string value from server containing 1's and 0's, then break that
    data = json.loads(body.decode("utf-8"))  # use body.decode("utf-8") to convert from bytes to string
    #json.loads("{\"GPIOStatuses\":\"00000\"}")
    lightStates = data["GPIOStatuses"]
    print(lightStates) #GPIOStates
    

    if "GPIOStatuses" in data: #GPIOStates
        for index, state in enumerate(data['GPIOStatuses']):
            GPIO.output(gpioList[index], int(state))
            lightStatesList.insert(index,state)

print(lightStatesList)
time.sleep(2)


'''
#FUNCTION Send Update to Server - 2s
#UpdateData - format to be {"GPIOState": "00001"}
updateData = {"notes":"Test"};

conn = http.HTTPConnection("pi-home-appliances.herokuapp.com")

#URL to be /GPIOStates and method to be PUT
conn.request("POST", "/notes", json.dumps(updateData),
             {"PiNo":piNo, "Content-type": "application/json"})
response = conn.getresponse()

print(response.status)
print(response.version)

body = response.read()
print(body)
conn.close()
'''
if GPIO.input(21):
    if lightStatesList[0] == "0":
        lightStatesList[0] = "1"
    elif lightStatesList[0] == "1":
        lightStatesList[0] = "0"

print(lightStatesList)
print(len(lightStatesList))

lightStates = "".join(lightStatesList) #Converting a list to a string and gets
# rid of the square brackets, commas and single quotation marks too

print("The updated states are: " + lightStates)

dictionary = {"GPIOStatuses":lightStates}

conn = http.HTTPConnection("pi-home-appliances.herokuapp.com")
conn.request("PUT", "/GPIOStatuses", json.dumps(dictionary),
             {"RPiNo":1, "Content-type":"application/json"})
response2 = conn.getresponse()

print(response2.version)
print(response2.status)
print(response2.reason)

if (response2.status >= 200) & (response2.status < 300):
    body = response2.read()
    print("PUT REQUEST 1")
    print(body)
    #conn2.close()

conn = http.HTTPConnection("pi-home-appliances.herokuapp.com")
conn.request("GET", "/GPIOStatuses", None, {"rpino":1}) #/notes, header={"PiNo:PiNo"}
response3 = conn.getresponse()

print(response3.status)
print(response3.version)

#body = response.read()
#conn.close()

if (response3.status >= 200) & (response3.status < 300):
    body = response3.read()
    print("GET REQUEST 2")
    print(body)
    conn.close()

print("End of test program")    

