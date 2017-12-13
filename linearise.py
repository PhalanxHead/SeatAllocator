#!/etc/python3

"""
Author:     PhalanxHead
Date:       13/12/2017
Name:       linearise.py
Purpose:    Takes the output CSV of the seatAllocator program (or a slightly
            modified version of it) and rearranges it to be in the format of
            the initial file given (ie: lastName, firstName, tableNumber).

            Writes back to a CSV file.


            Released Under Apache License 2.0 (See ReadMe)
"""

# *** IMPORTS ***
import csv
import sys
import os
import errno

# *** DEFAULTS ***
DEF_FILEOUT = "Linear"
DEF_OUTDIR = "LinearForm/"
DEF_TABLEDIR = "TableForm/"


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

def findTable(name, tableFile):
    """
    Searches through the table file specified by tableFIle until the given name string is
    found. Returns the table number the name was found on.
    """

    if "\\" not in tableFile and "/" not in tableFile:
        tableFile = DEF_TABLEDIR + tableFile

    with open(tableFile, 'r') as tf:
        tfReader = csv.reader(tf)
        tableNum = 0

        # Skip header line
        next(tfReader)

        for line in tfReader:
            tableNum = line[0]
            for cell in line[1:]:
                if cell == name:
                    return tableNum

        return 0


# ******* MAIN *******

listFile = input("Enter your initial list file name: ")
tableFile = input("Enter your table file name: ")
outFile = input("Enter a file to write to: ")

try:
    # Open all the read-in files
    with open(listFile, 'r') as lf:
        # Create the new outFile
        make_sure_path_exists(DEF_OUTDIR)
        with open(DEF_OUTDIR + outFile + ".csv", 'w') as of:

            lfReader = csv.reader(lf)
            ofWriter = csv.writer(of)

            for row in lfReader:
                if row[2] != "":
                    ofWriter.writerow(row)
                    continue

                else:
                    name = ' '.join(row[::-1])
                    tableNum = findTable(name, tableFile)
                    ofWriter.writerow((row[0], row[1], tableNum))

except:
    print("Error! ", sys.exc_info()[1])

print("Done!!!")
print("Output at ", DEF_OUTDIR + outFile + ".csv")

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
