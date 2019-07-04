# ****************************************************************************
# 
# FILE LINK MIGRATION TOOL
#
# 2019 JACOB HANSEN
# ______________________________
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# PURPOSE
# ______________________________
# 
# The Purpose of this tool is to determine the relationship between files located in separate locations,
# and provide a CSV file linking the files and their relative links within both locations. 
#
# INPUT
# ______________________________
# The input of this program must be two .CSV files formatted as follows:
#
# File 1: CurrentRecordLinks.csv
# [LINK ID],[RECORD ID],[CUSTOMER/VENDOR],[URL1],[FILE NAME] **HEADER ROW MUST NOT BE PRESENT**
# ...
#
# File 2: NewLocationFiles.csv
# [FILENAME], [FILEPATH], [SIZE], [EXTENSION] **HEADER ROW MUST NOT BE PRESENT**
# FILE SIZE IS NOT REQUIRED FOR CURRENT VERSION
# ...
# var = raw_input("Text Here")

import csv
import sys
import os
from datetime import datetime
import logging
import time

logging.basicConfig(level = logging.INFO, filename = time.strftime("logs/RecordLinkReconciler-%Y-%m-%d.log"))
logpath = time.strftime("logs/RecordLinkReconciler-%Y-%m-%d.log")

os.system('clear')
print("Record Link Reconciliation Tool")
print("2019 Jacob Hansen")
print("\n")
print("This program is free software: you can redistribute it and/or modify")
print("it under the terms of the GNU General Public License as published by")
print("the Free Software Foundation, either version 3 of the License, or")
print("(at your option) any later version.")
print("\n")

# Create Global Variables
CurrentRecordLinksCounter = 0
NewLocationCounter = 0
NewLocationFiles = set()
CurrentRecordLinksFiles = set()
OldToNew = []
ErrorNum = 0

ReconciliationSet = set()
ReconciledLinksCounter = 0

# Write all New Location Files to set 'NewLocationFiles'
with open('UpdatedNewLocationFiles.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        allData = ((row[1]).split('/'))
        allData.append(row[0])
        address = (allData[-2:])

        oldPath = ''
        for item in allData:
            oldPath += item + '\\'

        oldPath = oldPath[:-1]
        line = oldPath + '|'

        #print(str(address[-2]) + '\\' + str(address[-1]))

        
        # Try to find file name and parent folder (To catch error if file is in root folder)
        try:
            line += address[-2] + '\\' + address[-1]
        except:
            ErrorNum += 1

        NewLocationFiles.add(line)
        NewLocationCounter += 1

print('Total Files in New Location Skipped due to Errors: ' + str(ErrorNum))
print('Total Files Found in New Location: ' + str(NewLocationCounter))

#Write all Current Record Link Files to set 'CurrentRecordLinksFiles'
# 'line' Definition: [oldPath],[address],[Record ID],[Customer/Vendor]
with open('UpdatedRecordLinks.csv') as csvDataFile:
    csvReader2 = csv.reader(csvDataFile)
    for row in csvReader2:
        allAddress = str(row[3]) + '\\' + str(row)
        allData = ((row[3]).split('\\'))
        address = (allData[-2:])

        oldPath = ''
        for item in allData:
            oldPath += item + '\\'
        #oldPath  += '\\' + str(row[0])

        line = oldPath + '|'
        
        # Try to find file name and parent folder (To catch error if file is in root folder)
        try:
            line += address[-2] + '\\' + address[-1]
        except:
            ErrorNum += 1

        line += '|' + row[0] + '|' + row[1]

        CurrentRecordLinksFiles.add(line)
        CurrentRecordLinksCounter += 1

print('Total Files in Current Location Skipped due to Errors: ' + str(ErrorNum))
print('Total Files Found in Current Location: ' + str(CurrentRecordLinksCounter))
print("\n")

start=datetime.now()

i = 0
length = len(CurrentRecordLinksFiles)

for item in CurrentRecordLinksFiles:
    RecordLinkFile = item.split('|')
    i += 1
    timeTaken = datetime.now()-start
    seconds = round(timeTaken.total_seconds(),2)
    unroundedMinutes = seconds/60
    minutes = round(unroundedMinutes,2)
    percentDone = i/length
    estimatedTime = percentDone/timeTaken.total_seconds()
    print('\r' + 'Progress: ' + str(i) + ' / ' + str(length) + ' Time Elapsed: ' + str(minutes)+ ' min' + '\r')
    sys.stdout.write("\033[F")
    #print(RecordLinkFile[1])
    for item2 in NewLocationFiles:
        try:
            NewLocationFile = item2.split('|')
        except:
            ErrorNum += 1
        #print(NewLocationFile[1])
        if(RecordLinkFile[1] == NewLocationFile[1]):
            # appendLine Definition: [RecordLinkFile Name],[CurrentRecordLink ID],[CurrentRecordLinkURL],[NewLocationURL]
            appendLine = RecordLinkFile[1] + ',' + RecordLinkFile[2] + ',' + RecordLinkFile[0] + ',' + NewLocationFile[0]
            ReconciliationSet.add(appendLine)
            ReconciledLinksCounter += 1

print("\n")
print("Finished Searching, Writing to CSV.")
print("\n")
print("Process Completed")
print(str(ReconciledLinksCounter) + " Links Reconciled, " + str(length-ReconciledLinksCounter) + " Reconciliation Paths not Found")
print("Logs are available here: " + str(logpath))
print("\n")
print(length)
print(ReconciledLinksCounter)
# Write Data to CSV

f = open("Reconciliation.csv", "w")
f.truncate()
f.close()

with open('Reconciliation.csv', 'a') as csvDataFile:
    writer = csv.writer(csvDataFile)
    header = ['RecordLinkFile Name','CurrentRecordLink ID','CurrentRecordLinkURL','NewLocationURL']
    writer.writerow(header)
    for item in ReconciliationSet:
        line = [item]
        writer.writerow(line)
csvDataFile.close()
