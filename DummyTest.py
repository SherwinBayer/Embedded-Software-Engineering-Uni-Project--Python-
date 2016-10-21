'''import ProjectSetup as setup
import ProjectGetState as get'''

import RaspberryPiLight as obj
import time


piOne = obj.RaspberryPiLight(1,"pi-home-appliances.herokuapp.com","/GPIOStatuses")
piOne.getPiNumber()
piOne.getHostName()
piOne.getURL()
piOne.setup()
#counter = 0
while(1):    
    piOne.getStates()
    #counter += 1
    #if counter >= 5:
    time.sleep(1)
    piOne.updateStates()
    #    counter = 0
    #counter += 1

    #if counter == 3:
        #piOne.addNewComponents()
    
    #if counter >= 5:
        #break
    #time.sleep(1)

#piOne.cleanup()



