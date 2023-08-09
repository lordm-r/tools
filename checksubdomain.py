import requests
import json

url="https://domains.yougetsignal.com/domains.php"
site=input("enter your site: ")

data_selected={"remoteAddress":f"{site}"}

http=requests.post(url,data=data_selected).text
data = json.loads(http)
for subdomain in data["domainArray"]:
    print(subdomain[0])
