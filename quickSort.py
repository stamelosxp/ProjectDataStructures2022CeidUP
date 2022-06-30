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

def quickSortDate(data):
    if len(data) < 2:
        return data
    lessthan, equalto, greaterthan = [], [], []
    pivot = datetime.strptime(data[0][0], '%m/%d/%Y').date()
    for i in range(0, len(data)):
        tempDate = datetime.strptime(data[i][0], '%m/%d/%Y').date()
        if tempDate < pivot:
            lessthan.append(data[i])
            data[i], data[0] = data[0], data[i]
        elif tempDate == pivot:
            equalto.append(data[i])
        elif tempDate > pivot:
            greaterthan.append(data[i])

    return quickSortDate(lessthan) + equalto + quickSortDate(greaterthan)


def quickSortTemperature(data):
    if len(data) < 2:
        return data
    lessthan, equalto, greaterthan = [], [], []
    pivot = float(data[0][1])
    for i in range(0, len(data)):
        if float(data[i][1]) < pivot:
            lessthan.append(data[i])
            data[i], data[0] = data[0], data[i]
        elif float(data[i][1]) == pivot:
            equalto.append(data[i])
        elif float(data[i][1]) > pivot:
            greaterthan.append(data[i])

    return quickSortTemperature(lessthan) + equalto + quickSortTemperature(greaterthan)




dataDateSorted = quickSortDate(data)
dataTemperatureSorted = quickSortTemperature(dataDateSorted)
end = time.perf_counter()
for row in dataTemperatureSorted:
    print(row)

print("\nQuick Sort")
print(f"Time taken is {end - start}")