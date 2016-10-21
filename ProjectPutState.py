import sys
import ProjectSetup as setup
import http.client as http
import json

#This function will help update the data stored on the database within the web
#server if a button is physically pressed. 
def putLightStates(piNo, hostName, url):
    key = url[1:]#key is "GPIOStatuses", slicing the URL b/c its the same as the key
    #minus the forward slash

    #Checks iteratively whether a button which is connected up to a corresponding
    #GPIO input pin is pressed. If a button is pressed, then update the state of
    #the corresponding LED in the lightStatesList. NOTE: The actual LED will only
    #update the next time getLightStates function is called

    #This flag variable will be used determine when a request to the server
    #should be made i.e. When the state of an LED is to be changed because of a
    #button being pressed. Reason for this is b/c in the main while(1) loop,
    #the get and put methods will be called fairly quickly, hence we need to
    #provide the server with enough time for it to update the state values incase
    #the user on the app, decides to modify the LED states. 
    stateChanged = 0
    for i in range(0,len(setup.gpioInputList),1): #5 for default length!
        if setup.GPIO.input(setup.gpioInputList[i]):
                            if setup.lightStatesList[i] == "0":
                                setup.lightStatesList[i] = "1"
                                stateChanged = 1
                            elif setup.lightStatesList[i] == "1":
                                setup.lightStatesList[i] = "0"
                                stateChanged = 1

    if stateChanged == 1:
        lightStates = "".join(setup.lightStatesList)#Converting lightStatesList into
        #a String which will be sent to the web server
        print("The updated states which are to be sent to the server are: " + lightStates)
        updateData = {key:lightStates}#The data sent to the server will be sent as a
        #Python dictionary which will then be converted into a Javascript document
        #so the web server can properly update the database
        
        try:
            conn = http.HTTPConnection(hostName)#Setting up an HTTP connection
            conn.request("PUT", url, json.dumps(updateData),
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

        except http.HTTPException:
            print("Error connecting to Web Server")
        except ValueError:
            print("Potential error with JSON Decoding")
        except:
            print("Unexpected error", sys.exc_info()[0])

