import time
import datetime
import urllib
import json
import urllib.request
import pygeoip
import csv
from lib.defineEntries import defineEntries

################################################################################
def getIPlog(row, IPcount, dates, lookFor):
    entries = defineEntries(row, 'IP')
    if (entries['event'].find(lookFor) != -1):
        IP = entries['IPAddress'].split('[')[1].split(']')[0]
        date = entries['date']
        timeStamp =  entries['time']
        dates.append(date +' '+ timeStamp)
        string = '%s    %s  %s' % (date, timeStamp, IP);
        IPcount.append(IP)
    else:
        string = ''

    return string, IPcount, dates;
################################################################################
def getTimeBetweenDates (firstDate, finalDate):
    try:
        t1 = time.mktime(time.strptime(firstDate, '%m/%d/%Y %H:%M:%S'))
        t2 = time.mktime(time.strptime(finalDate, '%m/%d/%Y %H:%M:%S'))
    except:
        t1 = time.mktime(time.strptime(firstDate, '%Y/%m/%d %H:%M:%S'))
        t2 = time.mktime(time.strptime(finalDate, '%Y/%m/%d %H:%M:%S'))

    return str(datetime.timedelta(seconds=t2-t1))

################################################################################
def getIPaddress(ip):
    urlFoLaction = ("http://www.freegeoip.net/json/" + ip)
    with urllib.request.urlopen(urlFoLaction) as url:
        locationInfo = json.loads(url.read())
        stringIPlocation = ('IP: ' + str(locationInfo['ip']) +
        ', Country: ' + locationInfo['country_name'] +
        ', City: ' + locationInfo['city'] +
        ', Latitude: ' + str(locationInfo['latitude']) +
        ', Longitude: ' + str(locationInfo['longitude']))

    return stringIPlocation;

###############################Write Output File ###############################
def writeOutputIPanalysis(reader,filename, lookfor):
    exit = 0;
    with open(filename, 'w+') as fileLog:
        fileLog.write('Date\tTime\tIP Address\n')
        IPcount = []
        dates = []

        for row in reader:
            string, IPcount, dates = getIPlog(row, IPcount, dates, lookfor);
            if len(string) != 0 :
               fileLog.write(string + '\n')

        if len(IPcount) != 0:
            IPunique = list(set(IPcount))
            IPcount = len(IPunique)
            timeDuration = getTimeBetweenDates (dates[0],  dates[len(dates)-1])

            fileLog.write('\nThis user has %d unique IP addresses in %s\n' % (IPcount, timeDuration))
            fileLog.write('\nList of Unique IPs:')
            for ip in IPunique:
               stringIPlocation = getIPaddress(ip)
               fileLog.write('\n' + stringIPlocation)

            exit = 1 #If found the correct log


    return exit
