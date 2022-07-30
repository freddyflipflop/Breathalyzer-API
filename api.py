from urllib import response
import requests
import os
import json
#Add url for detection
url_detect = ""

def switch(alcohol_content):
    okay_msg = "Happy Journey"
    not_okay_msg = "Stay where you are"
    state_on = "HIGH"
    state_off = "LOW"
    url = "https://cloud.boltiot.com/remote/APIKEY/digitalWrite"
    headers = {
        'Cache-Control': "no-cache"
        }
    if(alcohol_content < 800):
        querystring = {"pin":"0","state":state_on,"deviceName":"DEVICENAME"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        print(okay_msg)
    elif(alcohol_content > 800):
        querystring = {"pin":"0","state":state_off,"deviceName":"DEVICENAME"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        print(not_okay_msg)

def connect_to_bolt(url_detect):
    response = requests.get(url_detect)
    data=response.json()
    print(data)
    #return data
    alcohol_content = int(data["value"])
    switch(alcohol_content)
if __name__ == "__main__":
    connect_to_bolt(url_detect)














