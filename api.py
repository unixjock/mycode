#!/usr/bin/python3

import requests
def main():
    astros = requests.get("http://api.open-notify.org/astros.json")
    astrodata = astros.json()
    #print(astrodata)
    print(astrodata.get("people"))
    print(astrodata.get("people")[1])
    print(astrodata.get("people")[1].get("name"))

main ()

