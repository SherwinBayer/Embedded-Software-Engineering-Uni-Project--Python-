import ProjectSetup as setup
import ProjectGetState as get
import time
import ProjectPutState as put
import ProjectAdditionalComponents as comp

#NOTE: This entire project is based on the notion that the same GPIO pins for
#input and output will always be used for each Raspberry Pi that this program is
#loaded onto. Also, this assumes that exactly 5 LED's and 5 buttons are connected
#to the respective header pins.

class RaspberryPiLight:

    def __init__(self, piNo, hostName, url):
        self.piNo = piNo
        self.hostName = hostName #"pi-home-appliances.herokuapp.com"
        self.url = url #"/GPIOStates"

    def setup(self):
        setup.setup()
    
    def getStates(self):
        get.getLightStates(self.piNo, self.hostName, self.url)

    def getPiNumber(self):
        print("This raspberry pi number is: " + str(self.piNo))

    def getHostName(self):
        print("The host name(web server) you are attempting to connect to is called: " + self.hostName)

    def getURL(self):
        print("The URL which will be requested is: " + self.url)

    def setNewHostName(newHostName):
        self.hostName = newHostName

    def setNewURL(newURL):
        self.url = newURL

    def updateStates(self):
        put.putLightStates(self.piNo, self.hostName, self.url)

    #This function will require more work! Will not be ready by the due date
    def addNewComponents(self):
        comp.addNewLED(self.piNo, self.hostName, self.url) 

    def cleanup(self):
        setup.GPIO.cleanup()


'''piOne = RaspberryPiLight(1,"pi-home-appliances.herokuapp.com","/GPIOStatuses")
piOne.setup()
piOne.getStates()'''     
