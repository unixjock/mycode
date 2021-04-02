#!/usr/bin/python3
''' Monty Python  Bridge'''

def main():
    # lOOP
    while True:
        print("What is your favorite color? ", end="")
        # Get user input
        color=input()
        ## Depends on color
        if color == "blue":
            message="No... RED!"
        elif color == "red":
            message="No,,, Blue"
        elif color == "":
            print ("ERROR,enter your favoite color")
            message="enter Color"
        else:
            message="color, you may pass"
            break
        print(message)

if __name__ == "__main__":
    main()
