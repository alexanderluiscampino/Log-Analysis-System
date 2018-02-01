import urllib
import json
import urllib.request
import pygeoip
import time

ip = '186.94.126.8'
start = time.clock() #Measures time taken to create files
urlFoLaction = ("http://www.freegeoip.net/json/" + ip)
with urllib.request.urlopen(urlFoLaction) as url:
      locationInfo = json.loads(url.read())
      stringIPlocation = ('IP: ' + str(locationInfo['ip']) +
      ', Country: ' + locationInfo['country_name'] +
      ', City: ' + locationInfo['city'] +
      ', Latitude: ' + str(locationInfo['latitude']) +
      ', Longitude: ' + str(locationInfo['longitude']))

print(str(int(time.clock() - start)))
print(stringIPlocation);
