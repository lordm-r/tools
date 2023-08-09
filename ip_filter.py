import requests
import os
#this is appication find  your location city and country
os.system("cls")
my_ip=requests.get("https://api.ipify.org/").text
my_localtion=requests.get(f"https://ipapi.co/{my_ip}/country/").text
my_city=requests.get(f"https://ipapi.co/{my_ip}/city/").text
print(my_city)
print(my_localtion)