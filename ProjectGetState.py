import sys
import ProjectSetup as setup
import http.client as http
import json

#This function will attempt to setup an HTTP connection with the web server
#and retrieve the data from the database. This data will be used to set the state
#of the LED's 
def getLightStates(piNo, hostName, url):
    data = {} #This will hold the retrieved data is sent in the
    #HTTP response's body
    key = url[1:] #key is "GPIOStatuses", slicing the URL b/c its the same as the key
    #minus the forward slash
    try:
        conn = http.HTTPConnection(hostName)#Setting up an HTTP connection
        conn.request("GET", url, None, {"rpino":piNo})#Requesting the web server
        #with the Raspberry Pi's no. (specified when creating the RaspberryPiLight
        #object) sent as a header
        response = conn.getresponse() #Obtaining server response
        version = response.version
        status = response.status
        reason = response.reason
        print("HTTP version used: " + str(version))
        print("HTTP status code: " + str(status))
        print("Reason: " + reason)

        if (status >= 200) & (status < 300): #If response is OK
            body = response.read()
            print(body)
            conn.close() #Read the response's body and close the connection
            data = json.loads(body.decode("utf-8"))#The data sent from the server
            #is in the form of a Javascript document, this converts the document
            #to a Python object, The data is also converted from bytes into a
            #String using the utf-8 character encoding
            #data = json.loads("{\""+key+"\""+":" + "\"00000\"}")
            print(data[key])

    except http.HTTPException:
        print("Error connecting to Web Server")
    except ValueError:
        print("Potential error with JSON Decoding")
    except:
        print("Unexpected error", sys.exc_info()[0])
        
    #By enumerating the data, the index can be used to control the corresponding
    #GPIO output pin for the LED's, the state will either be equal to a 1 or 0
    #based on data sent by the response, this will drive the LED's high or low.
    #The state of each LED is also stored in the lightStatesList (Will be used
    #to help determine what the LED's should do when a button on the breadboard
    #is pressed.
    if key in data:
        for index, state in enumerate(data[key]):
            setup.GPIO.output(setup.gpioList[index], int(state))
            if len(setup.lightStatesList) <= index:
                setup.lightStatesList.append(state)
            else:
                setup.lightStatesList[index] = state

     
    
