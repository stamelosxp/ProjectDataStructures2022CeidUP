import csv
import math
from datetime import datetime
import time

file = open(r"ocean.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data = []
for row in csvreader:
    data.append(row)

file.close()


def Menu(data):
    start = time.perf_counter()
    print("Menu: ")
    print("1.Search Date.")
    print("2.Exit")

    userChoice = int(input("Insert your choice: "))
    while(True):
        if (userChoice == 1):
            insertDate = input("Insert Date (m/d/y): ")
            userDate = datetime.strptime(insertDate, '%m/%d/%Y')
            userDate = userDate.date()
            dataDateSorted = quicksortDate(data)
            pos = bisDate(dataDateSorted, userDate, 0, len(dataDateSorted) - 1)
            if (pos == -1):
                print("\nThis value doesn't exist in list!\n")
                end = time.perf_counter()
                print("\nBest-Case Binary Interpolation Search")
                print(f"Time taken is {end - start}", "\n")
                Menu(data)
            else:
                print("\nDate: ", pos[0])
                print("Temperature: ", pos[1])
                print("Phosphate: ", pos[2])
                print("\n")
                end = time.perf_counter()
                print("\nBest-Case Binary Interpolation Search")
                print(f"Time taken is {end - start}", "\n")
                Menu(data)
        elif (userChoice == 2):
            print("Closing...")
            time.sleep(2)
            exit(0)
        else:
            print("\nPlease Try Again!")
            userChoice = int(input("Insert your choice: "))



def quicksortDate(data):
    if len(data) < 2:
        return data
    low, same, high = [], [], []
    dateValue1 = data[0][0]
    dateObject1 = datetime.strptime(dateValue1, '%m/%d/%Y')
    pivot = dateObject1.date()

    for i in range(0, len(data)):
        dateValue = data[i][0]
        dateObject = datetime.strptime(dateValue, '%m/%d/%Y')
        tempValue = dateObject.date()

        if tempValue < pivot:
            low.append(data[i])
            data[i], data[0] = data[0], data[i]

        elif tempValue == pivot:
            same.append(data[i])

        elif tempValue > pivot:
            high.append(data[i])


    return quicksortDate(low) + same + quicksortDate(high)



def bisDate(data, value, left, right):

    leftDate = datetime.strptime(data[left][0], '%m/%d/%Y').date()

    rightDate = datetime.strptime(data[right][0], '%m/%d/%Y').date()
    if value < leftDate or value > rightDate:
        return -1
    if left > right or (left == right and leftDate != value):
        return -1
    elif left == right and leftDate == value:
        return data[left]

    tempPos = (value-leftDate).days / (rightDate-leftDate).days

    midPos = (int)(left + tempPos*(right-left))


    i = 1

    midDate = datetime.strptime(data[midPos][0], '%m/%d/%Y').date()

    if value > midDate:

        while True:
            nextPos = midPos + i * math.ceil(math.sqrt(len(data)))

            nextDate = datetime.strptime(data[nextPos][0], '%m/%d/%Y').date()

            if nextPos > right or value < nextDate:
                break
            if value == nextDate:
                return data[nextPos]

            i *= 2

        left = midPos + (i-1)*math.ceil(math.sqrt(len(data)))+1
        right = min(right, nextPos-1)


        return bisDate(data, value, left, right)

    elif value < midDate:

        while True:
            nextPos = midPos - i * math.ceil(math.sqrt(len(data)))

            nextDate = datetime.strptime(data[nextPos][0], '%m/%d/%Y').date()

            if nextPos < left or value > nextDate:
                break
            if value == nextDate:
                return data[nextPos]

            i *= 2

        right = midPos - (i - 1) * math.ceil(math.sqrt(len(data))) - 1
        left = min(left, nextPos + 1)

        return bisDate(data, value, left, right)
    else:
        return data[midPos]

Menu(data)