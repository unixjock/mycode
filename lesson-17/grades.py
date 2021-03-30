#!/usr/bin/python3

print("What is your quest?")
quest= input()

def main():
    if quest == "Monty":
        message="Match -> Monty"
    elif quest == "Python":
        message="-> Match: Python"
    elif quest == "":
        print("ERROR,enter Quest")
        exit()
    else:
        message=quest
    print(message)

if __name__ == "__main__":
    main()
