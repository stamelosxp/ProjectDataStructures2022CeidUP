import csv
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
            pos = binarysearchDate(dataDateSorted, userDate, 0, len(dataDateSorted) - 1)
            if (pos == -1):
                print("\nThis date doesn't exist in list!\n")
                end = time.perf_counter()
                print("\nBinary Search")
                print(f"Time taken is {end - start}", "\n")
                exit(0)
                Menu(data)
            else:
                print("\nDate: ", pos[0])
                print("Temperature: ", pos[1])
                print("Phosphate: ", pos[2],"\n")
                end = time.perf_counter()
                print("\nBinary Search")
                print(f"Time taken is {end - start}", "\n")
                exit(0)
                Menu(data)

        elif (userChoice == 2):
            print("\nClosing...")
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


def binarysearchDate(data, value, left, right):

    leftDate = datetime.strptime(data[left][0], '%m/%d/%Y').date()
    rightDate = datetime.strptime(data[right][0], '%m/%d/%Y').date()
    if value < leftDate or value > rightDate:
        return -1

    midPos = (left + right) // 2

    tempDate = datetime.strptime(data[midPos][0], '%m/%d/%Y')
    tempDate = tempDate.date()
    if left<=right:
        if value == tempDate:
            return data[midPos]
        elif value < tempDate:
            return binarysearchDate(data, value, left, midPos - 1)
        else:
            return binarysearchDate(data, value, midPos + 1, right)
    else:
        return -1



while(True):
    Menu(data)
