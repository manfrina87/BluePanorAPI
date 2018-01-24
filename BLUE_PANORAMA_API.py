#!/usr/bin/python

import json
import time
import datetime
import requests
import sys



##ON DEVELOPMENT: find IATA code of airports
#airports=json.load(open('airports.json'))
#for airp in airports:
#    if airp['iso'] == 'IT' and airp['type'] == 'airport':
#        print airp['iata'],
#        print airp['name']


#Usage: python BLUE_PANORAMA_API.py 'MXP' 'HAV' ["1,ADULT","0,CHILD","0,INFANT"]
#origin=sys.argv[1]
#destination=sys.argv[2]
#passengers=sys.argv[3]

#Usage: python BLUE_PANORAMA_API.py
origin="MXP"
destination="HAV"
passengers=["1,ADULT","0,CHILD","0,INFANT"]

myurl="https://ibe-app.blue-panorama.com/ibe-rest-api/search/flight/calendar/fares"
triptype="OW"
now = datetime.datetime.now()
query_year=now.year
next_query_year=query_year+1
query_month= [('01', '02'), ('02', '03'), ('03', '04'), ('04', '05'), ('05', '06'), ('06', '07'), ('07', '08'), ('08', '09'), ('09', '10'), ('10', '11'), ('11', '12'), ('12', '01')]


#results=[]
for tpl_month in query_month:
    from_month=tpl_month[0]
    to_month=tpl_month[1]
    if to_month != "01":
        date_from=str(query_year)+"-"+from_month+"-01"
        date_to=str(query_year)+"-"+to_month+"-01"
    else:
        date_from=str(query_year)+"-"+from_month+"-01"
        date_to=str(next_query_year)+"-"+to_month+"-01"
    print "From: ",date_from, "To: ", date_to
    payload={'tripType': triptype, 'pax': passengers, 'ooa' : origin, 'oda': destination, 'od' : date_from, 'oed' : date_to}
    r=requests.get(myurl, params=payload)
    try:
        print r.json()['onwardFares']
        #results.append(r.json())
    except:
        print "No flight found!"
        pass
    time.sleep(5)

