import csv
import time
from datetime import datetime

file = open(r"ocean.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data = []
for row in csvreader:
    data.append(row)
file.close()

class DateNode:
    nodesCounters = 0
    def __init__(self, dataList):
        self.dateValue = datetime.strptime(dataList[0], '%m/%d/%Y').date()
        tempList = []
        tempList.append(float(dataList[1]))
        self.temperatureValue = tempList
        self.left = None
        self.right = None
        self.height = 1
        DateNode.nodesCounters += 1
    def __del__(self):
        DateNode.nodesCounters -= 1

    def apppendTemperatureValue(self, dataList):
        self.temperatureValue.append(float(dataList[1]))

class DateAvlTree:
    def getHeight(self, DateNode):
        if DateNode is None:
            return 0
        else:
            return DateNode.height

    def getBalance(self, DateNode):
        if DateNode is None:
            return 0
        else:
            return self.getHeight(DateNode.left) - self.getHeight(DateNode.right)

    def getMinValueNode(self, DateNode):
        if DateNode is None or DateNode.left is None:
            return DateNode
        else:
            return self.getMinValueNode(DateNode.left)

    def rightRotate(self, DateNode):
        tempNodeA = DateNode.left
        tempNodeB = tempNodeA.right
        tempNodeA.right = DateNode
        DateNode.left = tempNodeB
        DateNode.height = 1 + max(self.getHeight(DateNode.left), self.getHeight(DateNode.right))
        tempNodeA.height = 1 + max(self.getHeight(tempNodeA.left), self.getHeight(tempNodeA.right))
        return tempNodeA

    def leftRotate(self, DateNode):
        tempNodeA = DateNode.right
        tempNodeB = tempNodeA.left
        tempNodeA.left = DateNode
        DateNode.right = tempNodeB
        DateNode.height = 1 + max(self.getHeight(DateNode.left), self.getHeight(DateNode.right))
        tempNodeA.height = 1 + max(self.getHeight(tempNodeA.left), self.getHeight(tempNodeA.right))
        return tempNodeA

    def insertNode(self, dataList, rootDateNode):
        tempDate = datetime.strptime(dataList[0], '%m/%d/%Y').date()
        if rootDateNode is None:
            return DateNode(dataList)
        elif tempDate < rootDateNode.dateValue:
            rootDateNode.left = self.insertNode(dataList, rootDateNode.left)
        elif tempDate > rootDateNode.dateValue:
            rootDateNode.right = self.insertNode(dataList, rootDateNode.right)
        else:
            rootDateNode.apppendTemperatureValue(dataList)

        rootDateNode.height = 1 + max(self.getHeight(rootDateNode.left), self.getHeight(rootDateNode.right))
        balance = self.getBalance(rootDateNode)

        if balance > 1 and tempDate < rootDateNode.left.dateValue:
            return self.rightRotate(rootDateNode)
        if balance < -1 and tempDate > rootDateNode.right.dateValue:
            return self.leftRotate(rootDateNode)
        if balance > 1 and tempDate > rootDateNode.left.dateValue:
            rootDateNode.left = self.leftRotate(rootDateNode.left)
            return self.rightRotate(rootDateNode)
        if balance < -1 and tempDate < rootDateNode.right.dateValue:
            rootDateNode.right = self.rightRotate(rootDateNode.right)
            return self.leftRotate(rootDateNode)

        return rootDateNode

    def deleteNode(self, tempDate, rootDateNode):
        if rootDateNode is None:
            print("\nThis date doesn't exist in list!\n")
            return rootDateNode
        elif tempDate < rootDateNode.dateValue:
            rootDateNode.left = self.deleteNode(tempDate, rootDateNode.left)
        elif tempDate > rootDateNode.dateValue:
            rootDateNode.right = self.deleteNode(tempDate, rootDateNode.right)
        else:
            if rootDateNode.left is None:
                tempNode = rootDateNode.right
                print("\nDate deleted successfully!\n")
                rootDateNode = None
                return tempNode
            elif rootDateNode.right is None:
                tempNode = rootDateNode.left
                rootDateNode = None
                print("\nDate deleted successfully!\n")
                return tempNode
            tempNode2 = self.getMinValueNode(rootDateNode.right)
            rootDateNode.dateValue = tempNode2.dateValue
            rootDateNode.temperatureValue = tempNode2.temperatureValue
            rootDateNode.right = self.deleteNode(tempNode2.dateValue, rootDateNode.right)

        rootDateNode.height = 1 + max(self.getHeight(rootDateNode.left), self.getHeight(rootDateNode.right))
        balance = self.getBalance(rootDateNode)

        if balance > 1 and self.getBalance(rootDateNode.left) >= 0:
            return self.rightRotate(rootDateNode)

        if balance < -1 and self.getBalance(rootDateNode.right) <= 0:
            return self.leftRotate(rootDateNode)

        if balance > 1 and self.getBalance(rootDateNode.left) < 0:
            rootDateNode.left = self.leftRotate(rootDateNode.left)
            return self.rightRotate(rootDateNode)

        if balance < -1 and self.getBalance(rootDateNode.right) > 0:
            rootDateNode.right = self.rightRotate(rootDateNode.right)
            return self.leftRotate(rootDateNode)

        return rootDateNode

    def searchDate(self, strDate, rootDateNode):
        tempDate = datetime.strptime(strDate, '%m/%d/%Y').date()

        if rootDateNode is None:
            return False
        elif rootDateNode.dateValue == tempDate:
            return rootDateNode.temperatureValue
        elif rootDateNode.dateValue < tempDate:
            return self.searchDate(strDate, rootDateNode.right)

        return self.searchDate(strDate, rootDateNode.left)

    def editTemperature(self, userValue, strDate,  rootDateNode):
        tempDate = datetime.strptime(strDate, '%m/%d/%Y').date()

        if rootDateNode is None:
            return False
        elif rootDateNode.dateValue == tempDate:
            rootDateNode.temperatureValue.clear()
            rootDateNode.temperatureValue.append(float(userValue))
            return rootDateNode
        elif rootDateNode.dateValue < tempDate:
            return self.editTemperature(userValue, strDate, rootDateNode.right)

        return self.editTemperature(userValue, strDate, rootDateNode.left)

    def inorder(self, rootDateNode):
        if rootDateNode:
            self.inorder(rootDateNode.left), print(rootDateNode.dateValue), self.inorder(rootDateNode.right)




class TemperatureNode:
    nodesCounters = 0
    def __init__(self, dataList):
        tempList = []
        tempList.append(dataList[0])
        self.dateValue = tempList
        self.temperatureValue = float(dataList[1])
        self.left = None
        self.right = None
        self.height = 1
        TemperatureNode.nodesCounters += 1
    def __del__(self):
        TemperatureNode.nodesCounters -= 1

    def apppendDate(self, dataList):
        self.dateValue.append(dataList[0])

class TemperatureAvlTree:
    def getHeight(self, TemperatureNode):
        if TemperatureNode is None:
            return 0
        else:
            return TemperatureNode.height

    def getBalance(self, TemperatureNode):
        if TemperatureNode is None:
            return 0
        else:
            return self.getHeight(TemperatureNode.left) - self.getHeight(TemperatureNode.right)

    def rightRotate(self, TemperatureNode):
        tempNodeA = TemperatureNode.left
        tempNodeB = tempNodeA.right
        tempNodeA.right = TemperatureNode
        TemperatureNode.left = tempNodeB
        TemperatureNode.height = 1 + max(self.getHeight(TemperatureNode.left), self.getHeight(TemperatureNode.right))
        tempNodeA.height = 1 + max(self.getHeight(tempNodeA.left), self.getHeight(tempNodeA.right))
        return tempNodeA

    def leftRotate(self, TemperatureNode):
        tempNodeA = TemperatureNode.right
        tempNodeB = tempNodeA.left
        tempNodeA.left = TemperatureNode
        TemperatureNode.right = tempNodeB
        TemperatureNode.height = 1 + max(self.getHeight(TemperatureNode.left), self.getHeight(TemperatureNode.right))
        tempNodeA.height = 1 + max(self.getHeight(tempNodeA.left), self.getHeight(tempNodeA.right))
        return tempNodeA


    def insertNode(self, dataList, rootTemperatureNode):
        tempValue = float(dataList[1])
        if rootTemperatureNode is None:
            return TemperatureNode(dataList)
        elif tempValue < rootTemperatureNode.temperatureValue:
            rootTemperatureNode.left = self.insertNode(dataList, rootTemperatureNode.left)
        elif tempValue > rootTemperatureNode.temperatureValue:
            rootTemperatureNode.right = self.insertNode(dataList, rootTemperatureNode.right)
        else:
            rootTemperatureNode.apppendDate(dataList)

        rootTemperatureNode.height = 1 + max(self.getHeight(rootTemperatureNode.left), self.getHeight(rootTemperatureNode.right))
        balance = self.getBalance(rootTemperatureNode)

        if balance > 1 and tempValue < rootTemperatureNode.left.temperatureValue:
            return self.rightRotate(rootTemperatureNode)
        if balance < -1 and tempValue > rootTemperatureNode.right.temperatureValue:
            return self.leftRotate(rootTemperatureNode)
        if balance > 1 and tempValue > rootTemperatureNode.left.temperatureValue:
            rootTemperatureNode.left = self.leftRotate(rootTemperatureNode.left)
            return self.rightRotate(rootTemperatureNode)
        if balance < -1 and tempValue < rootTemperatureNode.right.temperatureValue:
            rootTemperatureNode.right = self.rightRotate(rootTemperatureNode.right)
            return self.leftRotate(rootTemperatureNode)

        return rootTemperatureNode


def searchMax(rootTemperatureNode):
    current = rootTemperatureNode
    while (current.right):
        current = current.right
    return current

def searchMin(rootTemperatureNode):
    current = rootTemperatureNode
    while (current.left):
        current = current.left
    return current



def Menu(data, hashTable):
    print("Menu: ")
    print("1.Create an AVL-Tree with dates.")
    print("2.Create an AVL-Tree with temperatures.")
    print("3.Create a Hash-Table with dates.")
    print("4.Exit")
    userChoice = int(input("Insert your choice: "))
    while(True):
        if userChoice == 1:
            dateAvlTree = DateAvlTree()
            rootDateNode = None
            for row in data:
                rootDateNode = dateAvlTree.insertNode(row, rootDateNode)
            print("AVL-Tree created successfully!")
            print("Number of Node Dates: ", DateNode.nodesCounters)

            while(True):
                print("\nAVL-Dates Menu: ")
                print("1)Print inorder AVL.")
                print("2)Search a temperature value by date.")
                print("3)Edit temperature value of a date.")
                print("4)Delete a date.")
                print("5)Back.")
                print("6)Exit.")
                userChoice1 = int(input("Insert your choice: "))
                if userChoice1 == 1:
                    dateAvlTree.inorder(rootDateNode)
                elif userChoice1 == 2:
                    insertDate = input("Insert Date (m/d/y): ")
                    result = dateAvlTree.searchDate(insertDate, rootDateNode)
                    if result == False:
                        print("\nThis date doesn't exist in list!\n")
                    else:
                        print("Date: ", insertDate)
                        print("Temperature: ", result)
                elif userChoice1 == 3:
                    insertDate = input("Insert Date (m/d/y): ")
                    userTemperature = input("Insert a float number for new temperature value: ")
                    rootDateNode = dateAvlTree.editTemperature(userTemperature, insertDate, rootDateNode)
                    if rootDateNode == False:
                        print("\nThis date doesn't exist in list!\n")
                    else:
                        print("Temperature modified successfully!")
                        print("Date: ", rootDateNode.dateValue)
                        print("New temperature value: ", rootDateNode.temperatureValue[0])
                elif userChoice1 == 4:
                    insertDate = input("Insert Date (m/d/y): ")
                    tempNodeCounters = DateNode.nodesCounters
                    tempDate = datetime.strptime(insertDate, '%m/%d/%Y').date()
                    rootDateNode = dateAvlTree.deleteNode(tempDate, rootDateNode)
                    if tempNodeCounters > DateNode.nodesCounters:
                        print("New number of Node Dates: ", DateNode.nodesCounters)

                elif userChoice1 == 5:
                    Menu(data, hashTable)
                elif userChoice1 == 6:
                    print("\nClosing...")
                    time.sleep(2)
                    exit(0)
                else:
                    print("\nPlease Try Again!")
                    userChoice1 = int(input("Insert your choice: "))
            Menu(data, hashTable)
        elif userChoice == 2:
            temperatureAvlTree = TemperatureAvlTree()
            rootTemperatureNode = None

            for row in data:
                rootTemperatureNode = temperatureAvlTree.insertNode(row, rootTemperatureNode)

            print("AVL-Tree created successfully!")
            print("Number of Node Dates: ", TemperatureNode.nodesCounters)

            while (True):
                print("\nAVL-Temperatures Menu: ")
                print("1)Search dates with minimum value of temperature.")
                print("2)Search dates with maximum value of temperature.")
                print("3)Back.")
                print("4)Exit.")
                userChoice2 = int(input("Insert your choice: "))
                if userChoice2 == 1:
                    minDate = searchMin(rootTemperatureNode)
                    print("Minimum value of temperature: ", minDate.temperatureValue)
                    print("Dates: ", minDate.dateValue)
                elif userChoice2 == 2:
                    maxDate = searchMax(rootTemperatureNode)
                    print("Maximum value of temperature: ", maxDate.temperatureValue)
                    print("Dates: ", maxDate.dateValue)
                elif userChoice2 == 3:
                    Menu(data, hashTable)
                elif userChoice2 == 4:
                    print("\nClosing...")
                    time.sleep(2)
                    exit(0)
                else:
                    print("\nPlease Try Again!")
                    userChoice2 = int(input("Insert your choice: "))

            Menu(data, hashTable)
        elif userChoice == 3:
            print("\nHash Table created successfully!")

            while (True):
                print("\nHash Table Menu: ")
                print("1)Search a temperature value by date.")
                print("2)Edit temperature value of a date.")
                print("3)Delete a date.")
                print("4)Back.")
                print("5)Exit.")
                userChoice3 = int(input("Insert your choice: "))

                if userChoice3 == 1:
                    insertDate = input("Insert Date (m/d/y): ")
                    result = searchDate(hashTable, insertDate)
                    if result == False:
                        print("\nThis date doesn't exist in list!\n")
                    else:
                        print("Date: ", result[0])
                        print("Temperature: ", result[1])
                elif userChoice3 == 2:
                    insertDate = input("Insert Date (m/d/y): ")
                    hashTable, check, newDateList = editTemperature(hashTable, insertDate)
                    if check:
                        print("Temperature modified successfully!")
                        print("Date: ", newDateList[0])
                        print("New temperature value: ", newDateList[1])
                elif userChoice3 == 3:
                    insertDate = input("Insert Date (m/d/y): ")
                    hashTable, check = deleteDate(hashTable, insertDate)
                    if check:
                        print("\nData deleted successfully!\n")
                    else:
                        print("\nThis date doesn't exist in list!\n")
                elif userChoice3 == 4:
                    Menu(data, hashTable)
                elif userChoice3 == 5:
                    print("\nClosing...")
                    time.sleep(2)
                    exit(0)
                else:
                    print("\nPlease Try Again!")
                    userChoice3 = int(input("Insert your choice: "))

            Menu(data, hashTable)

        elif userChoice == 4:
            print("\nClosing...")
            time.sleep(2)
            exit(0)
        else:
            print("\nPlease Try Again!")
            userChoice = int(input("Insert your choice: "))



def hashDate(strDate):
    sum = 0

    for char in strDate:
        if char.isdigit():
            sum += int(ord(char))

    return sum % 11


def insertDate(hashTable, strDate, temperatureValue):
    index = hashDate(strDate)
    tempList = hashTable[index]

    if tempList is None:
        tempList = []
        tempList.append([strDate, temperatureValue])

        del hashTable[index]
        hashTable.insert(index, tempList)
    else:
        tempList.append([strDate, temperatureValue])
        del hashTable[index]
        hashTable.insert(index, tempList)
    return hashTable

def editTemperature(hashTable, strDate):
    index = hashDate(strDate)
    tempList = hashTable[index]

    if tempList is None:
        return hashTable, False, None
    else:
        userTemperature = input("Insert a float number for new temperature value: ")
        userTemperature = float(userTemperature)
        for row in tempList:
            tempRowDate = datetime.strptime(row[0], '%m/%d/%Y').date()
            tempStrDate = datetime.strptime(strDate, '%m/%d/%Y').date()

            if tempRowDate == tempStrDate:
                tempListIndex = tempList.index(row)
                del tempList[tempListIndex]
                tempList.insert(tempListIndex, [strDate, str(userTemperature)])
                del hashTable[index]
                hashTable.insert(index, tempList)
                return hashTable, True, tempList[tempListIndex]

        return hashTable, False, None


def deleteDate(hashTable, strDate):
    index = hashDate(strDate)
    tempList = hashTable[index]

    if tempList is None:
        return hashTable, False
    else:
        for row in tempList:
            tempRowDate = datetime.strptime(row[0], '%m/%d/%Y').date()
            tempStrDate = datetime.strptime(strDate, '%m/%d/%Y').date()

            if tempRowDate == tempStrDate:
                tempList.remove(row)
                del hashTable[index]
                hashTable.insert(index, tempList)
                return hashTable, True
            else:
                return hashTable, False

def searchDate(hashTable, strDate):
    index = hashDate(strDate)
    tempList = hashTable[index]

    for row in tempList:
        tempRowDate = datetime.strptime(row[0], '%m/%d/%Y').date()
        tempStrDate = datetime.strptime(strDate, '%m/%d/%Y').date()

        if tempRowDate == tempStrDate:
            return row
    return False

hashTable = [None] * 11

for row in data:
    hashTable = insertDate(hashTable, row[0], row[1])


Menu(data, hashTable)