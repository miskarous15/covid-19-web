import csv

def createNewCSV(csvname):
    filename = csvname + ".csv"
    print(filename)
    with open(filename, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

createNewCSV('test1')
createNewCSV('test2')
createNewCSV('test3')
createNewCSV('test4')
createNewCSV('test5')