#!/usr/bin/python3

#import Regular expression module module
import re
files = input("enter the file: ")
#create an empty dictionary
each_string = {}
#Open the desired file
with open(files , 'r', newline='') as file:
    file_contents = file.read()
strings = re.split(r'\W+', file_contents, flags=re.IGNORECASE)

# with open(file, 'r', newline = '') as file:

#check each string in the file and process it"""
for string in strings:
    if string in each_string:
        each_string[string] +=1
    else:
        each_string[string] = 1

#print your output alphabetically"""
for string in each_string:
    print("(",string,": ",each_string[string], ")",sep = "",end = " ")
print("\n", end="")

#show the most used and least used word"""