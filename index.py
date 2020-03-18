# Bring in needed packaged
import csv

# Create a CSV
# input: file name, does not include .csv in it
# output: a csv file

def createNewCSV(csvname):
    filename = csvname + ".csv"
    print(filename)
    with open(filename, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#def pullData(): 
#def cleanData():

createNewCSV('dataset')
