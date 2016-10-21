import sys
import ProjectSetup as setup
import http.client as http
import json

#This function will be used when the user would like to add a new LED and new
#button dynamically after the program has first been run (Make sure the new
#components are physically added first and you are connecting those components
#to valid GPIO header pins on the Raspberry Pi)
def addNewLED(piNo, hostName, url):
    #Flag variables
    validOutputPinNo = 0
    validInputPinNo = 0
    printThis = 0    

    print("Here are the available GPIO pins left for configuration: " + ", ".join(str(i) for i in setup.gpioPinsAvail))
    try:
        perform = input("Please enter \"Y\"/\"N\" if you would like to configure")
        performL = perform.lower()

        if performL == "y":
            while validOutputPinNo != 1:
                outputPin = int(input("Please enter a GPIO pin no. that will be used to power the LED"))

                validOutputPinNo = 1
                printThis = 1

                for i in range(0,len(setup.gpioList),1):
                    if outputPin == setup.gpioList[i]:
                        print("This pin no. is already used by an LED, try again")
                        validOutputPinNo = 0
                        printThis = 0
                        break
                    if outputPin == setup.gpioInputList[i]:
                        print("This pin no. is already used by a Button, try again")
                        validOutputPinNo = 0
                        printThis = 0
                        break

                if (outputPin not in setup.gpioPinsAvail) & (printThis == 1):
                        print("This is not a GPIO pin, try again")
                        validOutputPinNo = 0
                            
            if validOutputPinNo == 1:    
                setup.gpioPinsAvail.remove(outputPin)
                print("Available GPIO pins left for configuration: " + ", ".join(str(i) for i in setup.gpioPinsAvail))

            while validInputPinNo != 1:
                inputPin = int(input("Please enter a GPIO pin no. that will be used for the button"))

                validInputPinNo = 1
                printThis = 1

                if inputPin == outputPin:
                    print("You just entered " + str(inputPin) + " to act as your new LED pin, try again")
                    validInputPinNo = 0
                    printThis = 0

                for i in range(0,len(setup.gpioList),1):
                    if inputPin == setup.gpioList[i]:
                       print("This pin no. is already used by an LED, try again")
                       validInputPinNo = 0
                       printThis = 0
                       break
                    if inputPin == setup.gpioInputList[i]:
                       print("This pin no. is already used by a Button, try again")
                       validInputPinNo = 0
                       printThis = 0
                       break

                if (inputPin not in setup.gpioPinsAvail) & (printThis == 1):
                   print("This is not a GPIO pin, try again")
                   validInputPinNo = 0
                   
            if validInputPinNo == 1:          
                setup.gpioPinsAvail.remove(inputPin)
                        
            #Assuming valid GPIO pins are entered and the flag variables are set, the
            #new GPIO pins are added to the existing and corresponding lists
            setup.gpioList.append(outputPin)
            setup.gpioInputList.append(inputPin)
            
            #Configure the new GPIO pins for input and output
            setup.GPIO.setup(outputPin,setup.GPIO.OUT)
            setup.GPIO.setup(inputPin,setup.GPIO.IN)
            print("New LED and Button successfully added and configured for use")

            updateData = {
                "PinNo": outputPin,
                "RoomID":1,
                "Status": "0"
            }
            conn = http.HTTPConnection(hostName)#Setting up an HTTP connection
            conn.request("POST", url, json.dumps(updateData),
                     {"rpino":piNo, "Content-type":"application/json"})
            #Requesting the web server, sending the updateData dictionary within
            #the request's body, with the Raspberry Pi's no. (specified when
            #creating the RaspberryPiLight object) sent as a header
            #del updateData[key]
            response = conn.getresponse()#Obtaining server response
            version = response.version
            status = response.status
            reason = response.reason
            print("HTTP version used: " + str(version))
            print("HTTP status code: " + str(status))
            print("Reason: " + reason)

            if (response.status >= 200) & (response.status < 300): #If response is OK
                body = response.read()
                print(body)
                conn.close() #Read the response's body and close the connection

        elif performL == "n":
            print("Configuration process aborted")
        else:
            print("Configuration process aborted")

    except http.HTTPException:
            print("Error connecting to Web Server")
    except ValueError:
        print("Value error has occured")
    #except:
        #print("Unexpected error", sys.exc_info()[0])

        #DELETE
        '''
    
            conn = http.HTTPConnection(hostName)#Setting up an HTTP connection
            conn.request("DELETE", url + "?PinNo=" + LEDPinYouAskUser, null, null)
    
        '''
