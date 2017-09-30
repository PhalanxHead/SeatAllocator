#!/etc/python3

"""
Author:     PhalanxHead
Date:       30/09/2017
Name:       seatAllocator.py
Purpose:    Takes a csv file of names (Last, First, <any other info>)
            and outputs a list of semi-random groups using MD5 hashing and
            a seed (which was taken from the user).
            Writes to a csv file.

            Applicable to more than just seating at tables but it's the
            first application I found for it.


            Released Under Apache License 2.0 (info below code, line 106)
"""


# *** IMPORTS ***
from datetime import datetime
from collections import defaultdict
from math import ceil
import csv
import hashlib
import sys
import random
import os
import errno

def make_sure_path_exists(path):
    """
    Creates directory if it doesn't exist, cross-platform.
    Code from user Heikki Toivonen:
https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

### DEFAULT OUTPUT DIRECTORY
DEF_OUT = "TableListings/"

# *** Initialise randomiser ***
filename = input("Enter your names list file name: ")
output = input("Enter a file to write to: ")

try:
    MAX_SEATS = abs(int(input("Enter the number of seats per table: ")))
except:
    MAX_SEATS = 8

manSeed = input("Enter a seed for the randomiser (Blank input can't be reproduced): ")

if output == "":
    output = "out"

if manSeed == "":
    manSeed = str(datetime.now())

random.seed(manSeed)
tables = defaultdict(list)

# ***** READ IN AND HASH ***************
# Will complain if anything doesn't work.
try:
    # Work out how many people you have coming
    numRows = sum(1 for line in open(filename))
    with open(filename) as csvfile:

        # Work out how many tables will be needed,
        # then start reading  the file.
        numTables = ceil(numRows / MAX_SEATS)
        nameReader = csv.reader(csvfile)

        # Skip the header line
        next(nameReader)

        for row in nameReader:
        # String all of the names together correctly (Comment this out with
        # '#'s if the names are already one field in the csv.)
            row = row[0:2]
            name = ' '.join(row[::-1])

            # Hash the names with the 'random' integer
            nameKey = hashlib.md5((name +
                    str(random.randint(0, 100000))).encode())
            nameKey = int(nameKey.hexdigest(), 16) % numTables

            # Probe the tables until you find one that has a spare space.
            # Guaranteed to be a spare space as we took the ceiling of
            # names/seatsPerTable
            while len(tables[nameKey]) >= MAX_SEATS:
                nameKey = (nameKey + 1) % numTables
            tables[nameKey].append(name)

except:
    print("Error! ", sys.exc_info()[1])

# *************** OUTPUT ****************
make_sure_path_exists(DEF_OUT)
try:
    with open(DEF_OUT + output + ".csv", 'w') as csvfile:
        tableWriter = csv.writer(csvfile)
        # Change Student to whatever you like if not using this where Student
        # would be appropriate
        tableWriter.writerow(["Table Number"] + ["Student"] * MAX_SEATS)
        tableNum = 1
        for table in tables.values():
            tableWriter.writerow([tableNum] + table)
            tableNum += 1
except:
    print("Error! ", sys.exc_info()[1])

print("Done!!")

"""
            Licensing Info:

            Copyright 2017 Luke Hedt (PhalanxHead)
            Licensed under the Apache License, Version 2.0 (the "License");
            you may not use this file except in compliance with the License.
            You may obtain a copy of the License at

                http://www.apache.org/licenses/LICENSE-2.0

            Unless required by applicable law or agreed to in writing, software
            distributed under the License is distributed on an "AS IS" BASIS,
            WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
            implied. See the License for the specific language governing
            permissions and limitations under the License.
"""
