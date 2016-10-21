# Embedded-Software-Engineering-Uni-Project--Python-
A month long project developed for one of my papers at Uni, in which me and my group made use of a Raspberry Pi

The project is a prototype of a Home Automation Lighting System, in which the user is able to control the lighting system within the rooms
of his/her house. The user can use the App to set, whether to turn on or off the lights within a room. The state of the lights would then be
sent to a public web server that stores the state values in a database. The web server would then send that data to the Raspberry Pi which
would allow the Pi to actuate the lights. Communication between the three components was done using HTTP while the transmission and decoding
of data was done using JSON. In addition to controlling the lights using the App, the lights can also be affected by physical switches within
the rooms, so if a switch was used to turn the lights on or off, the updated states of the lights would also be sent to the web server.

Since this was only a month long project done within university, we did not have access to an actual lighting system, hence we simulated 
the lighting system using LED's that was connected to a breadboard. The LED's would operate based on the logic being driven by the 
Raspberry Pi's GPIO header pins. To simulate the switches within the rooms, we made use of Push Buttons that was also connected to the same
breadboard while the logic pins was connected to the Pi's header pins. That way when a button was pressed, the state of the LED's would change
resulting in the updated state being sent to the web server and the database values would be updated likewise. 

These files contain the source code from my end ONLY! I was tasked with developing the code for the Raspberry Pi while my other two group members
worked on an Android App and the other, a public web server and database.
