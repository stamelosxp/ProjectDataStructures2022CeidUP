import csv
from datetime import datetime
import time

start = time.perf_counter()
file = open(r"ocean.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data = []
for row in csvreader:
    data.append(row)

file.close()


def insertionSortDate(data):
    for i in range(1, len(data)):
        tempDate = datetime.strptime(data[i][0], '%m/%d/%Y').date()


        j = i - 1
        while j >= 0 and tempDate < (datetime.strptime(data[j][0], '%m/%d/%Y').date()):
            data[j], data[j + 1] = data[j + 1], data[j]
            j -= 1


        data[j + 1][0] = tempDate.strftime('%m/%d/%Y')

    return data


def insertionSortTemperature(data):
    for i in range(1, len(data)):
        tempTemperature = float(data[i][1])

        j = i - 1
        while j >= 0 and tempTemperature < float(data[j][1]):
            data[j], data[j + 1] = data[j + 1], data[j]
            j -= 1

        data[j + 1][1] = tempTemperature

    return data

dataDateSorted = insertionSortDate(data)
dataTemperatureSorted = insertionSortTemperature(dataDateSorted)
end = time.perf_counter()

for row in dataTemperatureSorted:
    print(row)

print("\nInsertion Sort")
print(f"Time taken is {end - start}")