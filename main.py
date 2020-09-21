import json, requests, calendar, time, os

#Seneye Settings
username = 'email'
password = 'passwordhere'
TriggerTemp = 26

#Sensibo Settings
PODID = 'SensiboUDIDhere'
APIKey  = 'APIKEYhere'

Sensibopayload = '{"acState":{"fanlevel":"high","mode":"cool","on":true,"targettemperature":23.0}}'

url = ('https://api.seneye.com/v1/devices?user=%s&pwd=%s' % (username , password))
SensiboURL = ('https://home.sensibo.com/api/v2/pods/%s/acStates?apiKey=%s' % (PODID, APIKey))

# Grab seneye information
seneye = requests.get(url)

for tank in seneye.json():
    url=('https://api.seneye.com/v1/devices/%s?IncludeState=1&user=%s&pwd=%s' % (tank["id"], username, password))
    tankinfo = requests.get(url)
    CurrentTemp = int(float(tankinfo.json()['exps']['temperature']['curr']))
    print(CurrentTemp)

    if (CurrentTemp) >= TriggerTemp:
        print("Tank is to hot, triggering AC")
        requests.post(SensiboURL, data=Sensibopayload)
    else:
        print("Tank is all good")
