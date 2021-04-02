#!/usr/bin/python3
"""Learning to do API lookups"""

import requests

#API Location 
API = "http://api.open-notify.org/astros.json"

# Main funtion
def main():
    #Counter Variable
    counter = 0

    #Print Header
    print("Names:")

    #This will send an HTTP GET to the URI,EXPECTS a 200 response
    astros = requests.get(API)

    #json() is a METHOD avail to astros HTTP requests object
    astrodata = astros.json()

    # Set people var
    peoplevar = astrodata.get("people")
    
    #Loop through and just get names
    for i in peoplevar:
        #Name variable
        namevar = astrodata.get("people")[counter].get("name")

        # Print to screen
        print(namevar)

        # Increment counter
        counter = counter + 1

    # Print footer total
    print ("Total: ", counter)

main()
