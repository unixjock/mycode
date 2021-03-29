#!/usr/bin/env python3

# create a list called list1
animals = ["dog", "cat", "fox"]
# display list1
print(animals)
# display list1[1] which should only display arista_eos
print(animals[1])
# create a new list containing a single item
bugs = ["bee","fly","ant"]
fish = ["cod","koi"]
print("Created bugs list, extending animals")
# extend list1 by list2 (combine both lists together into a single list)
animals.extend(bugs)
print(animals)
print("Created fish list, extending animals")
animals.extend(fish)
print(animals)
