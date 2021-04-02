#!/usr/bin/python3
''' Python Certification Script - By David Ciaglia '''

## Import
import requests

## Constant
API = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY"

## Define Mian function
def main ():
    # This will send an HTTP GET to the URI
    # this EXPECTS a 200 response
    astros = requests.get(API)

    # json() is a METHOD avail to astros HTTP requests object
    astrodata = astros.json()

    #print(astrodata)

    #print(astrodata.get("people"))
    print(astrodata.get("id"))

    #print(astrodata.get("people")[1])

    #print(astrodata.get("people")[1].get("name"))

## Execute main fucntion
if __name__ == "__main__":
    main()
