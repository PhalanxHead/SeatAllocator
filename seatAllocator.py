#!/etc/python3

"""
Author:     PhalanxHead
Date:       30/09/2017 - 13/12/2017
Name:       seatAllocator.py
Purpose:    Takes a CSV file of names (Last, First, <any other info>)
            and outputs a list of semi-random groups using MD5 hashing and
            a seed (which was taken from the user).
            Writes to a CSV file.

            Applicable to more than just seating at tables but it's the
            first application I found for it.


            Released Under Apache License 2.0 (See ReadMe)
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

# *** DEFAULTS ***
DEF_SEATS = 8
DEF_FILEOUT = "Tables"
DEF_OUTDIR = "TableForm/"

# *** SETTINGS ***
"""
Output modes:
    0 - Default. Writes to inputted csv file name
    1 - Prints in terminal
"""
OUT_MODE = 0

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

def validateInput(outfile, seed, seatsPerTable):
    """
    Inputs default values if none are specified.
    """
    if outfile == "":
        outfile = DEF_FILEOUT

    if seed == "":
        seed = str(datetime.now())

    if seatsPerTable == "" or not seatsPerTable.isnumeric():
        seatsPerTable = DEF_SEATS
    else:
        seatsPerTable = abs(int(seatsPerTable))

    return outfile, seed, seatsPerTable

def allocateTable(name, tables, numTables):
                # Hash the names with the 'random' integer
                nameKey = hashlib.md5((name +
                        str(random.randint(0, 100000))).encode())
                nameKey = int(nameKey.hexdigest(), 16) % numTables

                # Probe the tables until you find one that has a spare space.
                # Guaranteed to be a spare space as we took the ceiling of
                # names/seatsPerTable
                while len(tables[nameKey]) >= seatsPerTable:
                    nameKey = (nameKey + 1) % numTables
                tables[nameKey].append(name)

# ****** MAIN *******

# *** Initialise randomiser ***
filename = input("Enter your names list file name: ")
if OUT_MODE == 0:
    outFile = input("Enter a file to write to: ")

seatsPerTable = input("Enter the number of seats per table: ")
manSeed = input("Enter a seed for the randomiser (Blank input can't be reproduced): ")

validIn = validateInput(outFile, manSeed, seatsPerTable)

outFile =validIn[0]
manSeed = validIn[1]
seatsPerTable = validIn[2]

random.seed(manSeed)
tables = defaultdict(list)
invitedList = []

# ***** READ IN ***************
# Will complain if anything doesn't work.
try:
    # Work out how many people you have coming that need a table number
    # Clunky, I know
    numRows = 0
    with open(filename) as csvfile:
        for row in csvfile:
            if row[2] != "":
                numRows += 1

    with open(filename) as csvfile:

        # Work out how many tables will be needed,
        # then start reading  the file.
        numTables = ceil(numRows / seatsPerTable)
        nameReader = csv.reader(csvfile)

        # Skip the header line
        next(nameReader)

        for row in nameReader:
        # String all of the names together correctly (Comment this out with
        # '#'s if the names are already one field in the csv.)
            # Skip guests with pre-determined tables!
            if row[2] != "":
                continue
            name = ' '.join(row[::-1])
            invitedList.append(name)

except:
    print("Error! ", sys.exc_info()[1])
    exit()

# Randomise the list of names
random.shuffle(invitedList)

# **************** ALLOCATE *************
for name in invitedList:
    allocateTable(name, tables, numTables)

# *************** OUTPUT ****************
if OUT_MODE == 0:

    # Add default if necessary
    if "\\" not in outFile and "/" not in outFile:
        outFile = DEF_OUTDIR + outFile

    make_sure_path_exists(outFile.rpartition('/')[0])

    try:
        with open(outFile + ".csv", 'w') as csvfile:
            tableWriter = csv.writer(csvfile)
            # Change Student to whatever you like if not using this where Student
            # would be appropriate
            tableWriter.writerow(["Table Number"] + ["Student"] * seatsPerTable)
            tableNum = 1
            for table in tables.values():
                tableWriter.writerow([tableNum] + table)
                tableNum += 1
    except:
        print("Error! ", sys.exc_info()[1])

elif OUT_MODE == 1:
    for table in tables.items():
        print(table)

print("Done!!")
print("Output at ", outFile + ".csv")

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
