import csv
import numpy as np
import time

start = time.perf_counter()
file = open(r"ocean.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data = []
for row in csvreader:
    data.append(row)


file.close()



def countingPhosphateSort(data):

    #find max and min value of phosphate
    max = 0.0
    min = 0.0
    for i in range(0, len(data)):
        if max < float(data[i][2]):
           max = float(data[i][2])

        if min > float(data[i][2]):
            min = float(data[i][2])

    #count the appears of elements
    countList = []
    n = 0
    for i in np.arange(min, max + 0.01, 0.01):
        counter = 0

        for k in range(0, len(data)):
            if(k==0 and i == 0.0):
                n=0
            if(k==0):
                n+=1
            if(round(i,2) == float(data[k][2])):
                counter+=1


        countList.append([round(i,2), counter])

    for value, count in countList:
            currentCount = count
            tempIndex = countList.index([value, count])

            if tempIndex < len(countList)-1:
                tempIndex = countList.index([value, count]) + 1

                nextCount = countList[tempIndex][1]
                nectValue = countList[tempIndex][0]
                del countList[tempIndex]
                countList.insert(tempIndex, [nectValue, currentCount + nextCount])


    sortedData = []
    for i in data:
        sortedData.append(i)


    for row in data:
        for value, count in countList:
            dataPosition = data.index(row)
            phosphateValue = float(row[2])

            if (value ==  phosphateValue):
                tempList = row
                countListPos = countList.index([value, count])

                del sortedData[count - 1]
                sortedData.insert(count - 1, tempList)
                del countList[countListPos]
                countList.insert(countListPos, [value, count-1])

    return sortedData



data = countingPhosphateSort(data)
end = time.perf_counter()
for row in data: print(row)

print("\nCounting Sort")
print(f"Time taken is {end - start}")