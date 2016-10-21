import http.client as http
import json
import sys

data = {"PinNo":17, "Status":"0"}

conn = http.HTTPConnection("pi-home-appliances.herokuapp.com")#Setting up an HTTP connection
#conn.request("DELETE", "/GPIOStatuses", json.dumps(data),
 #            {"rpino":1, "Content-type":"application/json"})
conn.request("DELETE", "/GPIOStatuses?PinNo=17", None, {"rpino":1})
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
