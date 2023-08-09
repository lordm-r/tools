import os

import requests

os.system("cls")

http=input("enter url: ")
if http[0:6]=="http://":
    pass
else:
    http="http://"+http
status_code=requests.get(http,verify=0).status_code
print (status_code)