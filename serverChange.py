import csv

f = open("UpdatedNewLocationFiles.csv", "w")
f.truncate()
f.close()

# Create Global Variables
officeFiles = set()
salesAndProductionFiles = set()

# line Definition: [FILE NAME],[ADDRESS],[SIZE],[EXTENSION]
with open('NewLocationFiles.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        fileName = row[0]
        address = ((row[1]).split('\\'))
        size = row[2]
        extension = row[3]

        if(address[0] == 'P:'):
            address[0] = 'https://company.sharepoint.com/sites/company/Shared%20Documents'
            totalPath = ''
            for item in address:
                totalPath += item + '/'
            totalPath = totalPath[:-1]

            line = fileName + ',' + totalPath + ',' + size + ',' + extension
            salesAndProductionFiles.add(line)

        elif(address[0] == 'O:'):
            address[0] = 'https://company.sharepoint.com/sites/company2/Shared%20Documents'
            totalPath = ''
            for item in address:
                totalPath += item + '/'
            totalPath = totalPath[:-1]

            line = fileName + ',' + totalPath + ',' + size + ',' + extension
            officeFiles.add(line)

# Write Data to CSV
with open('UpdatedNewLocationFiles.csv', 'a') as csvDataFile:
    writer = csv.writer(csvDataFile)
    for item in salesAndProductionFiles:
        line = [item]
        writer.writerow(line)
    for item in officeFiles:
        line = [item]
        writer.writerow(line)

csvDataFile.close()