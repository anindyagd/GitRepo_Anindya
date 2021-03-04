from flask import Flask

import urllib.request, urllib.parse 
import json, time
key = r'<google key>' ## provide the google key to access the google api

## Google RestApi which will return the state name when any address is provided 

def GoogGeoAPI(address,api="",delay=3):
  base = r"https://maps.googleapis.com/maps/api/geocode/json?"
  addP = "address=" + urllib.parse.quote_plus(address)
  GeoUrl = base + addP + "&key=" + api
  response = urllib.request.urlopen(GeoUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  #print (jsonData)
  if jsonData['status'] == 'OK':
    resu = jsonData['results'][0]
    State_Name='NULL'
    for i in resu['address_components']:
      if i['types'][0] == 'administrative_area_level_1':
        State_Name = i['long_name'] 
    finList = [State_Name]
  else:
    finList = [None]
  time.sleep(delay) #in seconds
  return finList

## This is an web application which takes address as end point and retun the state against that address in the web page. 

app = Flask(__name__)

@app.route('/<string:Address>/')
def hello(Address):
    geoR = GoogGeoAPI(address=Address,api=key,delay=0)
    return "The State Name for this Address is {}". format(', '.join(geoR))
    
if __name__ == '__main__':
 app.run()  ## you can provide host and port name based on requirement, if nothing is provided it will take default local host.