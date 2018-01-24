# Blue Panorama REST
Make requests to [Blue Panorama Airlines](https://www.blue-panorama.com/main) website, using its REST api.

## HTTP request

* Request: **GET**
* Endpoint: https://ibe-app.blue-panorama.com/ibe-rest-api/search/flight/calendar/fares

## Parameters

* TripType: **RT** | **OW** | **MC**
triptype=the type of flight you want to search
    1. RT=round trip (a/r), 
    2. OW=origin way (one way only), 
    3. MC=multichannel (multi-destiny)

* Pax: [(**int,ADULT**) & (**int,CHILD**) & (**int,INFANT**)]
pax=number of passengers for each category, put zero if none
    1. int,ADULT : N°Passengers [ > 11 yrs ]
    2. int,CHILD : N°Passengers [ 2-11 yrs]
    3. int,INFANT : N°Passengers [ < 2 yrs]

### Forward Flight
* Oda: **IATA_code**
oda=origin destination airport (forward flight, destination airport)

* Ooa: **IATA_code**
ooa=origin origin airport (forward flight, origin airport)

* Od: **yyyy-mm-dd**
od=origin date (forward flight, from day x)

* Oed: **yyyy-mm-dd**
oed=origin end date (forward flight, until day x)

### Return Flight
* Rda: **IATA_code**                   
rda=return destination airport (return flight, destination airport)

* Roa: **IATA_code**                   
roa=return origin airport (return flight, origin airport)

* Rd: **yyyy-mm-dd**              
rd=return date (return flight, from day x)

* Red: **yyyy-mm-dd**             
red=return end date (return flight, until day x)

**NB:** Time difference between od/oed or between rd/red must be <=1 month

## Examples (curl)

One way trips (OW) 

```sh
$ curl "https://ibe-app.blue-panorama.com/ibe-rest-api/search/flight/calendar/fares?tripType=OW&pax=1,ADULT&pax=0,CHILD&pax=0,INFANT&ooa=MXP&oda=HAV&od=2018-03-10&oed=2018-04-09"
```

Round trips (RT)

```sh
$ curl "https://ibe-app.blue-panorama.com/ibe-rest-api/search/flight/calendar/fares?tripType=RT&pax=1,ADULT&pax=0,CHILD&pax=0,INFANT&oda=HAV&ooa=MXP&od=2018-01-10&oed=2018-02-09&rda=MXP&roa=HAV&rd=2018-01-10&red=2018-02-09"
```

Multichannel trips (MC)

*To be implemented...*

## Examples (python)
Open `BLUE_PANORAMA_API.py` to see how to use Blue Panorama API with the Requests library.
Installation of Requests Security (`pip install requests[security]`) is highly recommended.





 


