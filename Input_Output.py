'''
    This program will be used to take as inout the name and age of the user and provide the year the user turns 100
    years old
'''

import datetime

name = input(" Please enter your name: ")
age = int(input(" Please enter your age: "))

current_year = datetime.datetime.now().year

time_to_100 = 100 - age

year_person_turns_100 = current_year + time_to_100

print(" You will turn 100 in the year " + str(year_person_turns_100))
