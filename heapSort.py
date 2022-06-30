import csv
import time

start = time.perf_counter()
file = open(r"ocean.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data = []
for row in csvreader:
    data.append(row)

file.close()

count = []

def heapify(data, n, pos):
    root = pos
    left = 2 * pos + 1
    right = 2 * pos + 2
    if left < n and float(data[root][2]) < float(data[left][2]):
        root = left
    if right < n and float(data[root][2]) < float(data[right][2]):
        root = right
    if root != pos:
        data[pos], data[root] = data[root], data[pos]
        heapify(data, n, root)

    return data


def heapSort(data):
    size = len(data)

    for i in range(size // 2 - 1, -1, -1):
        heapify(data, size, i)

    for i in range(size - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data


data = heapSort(data)
end = time.perf_counter()
for row in data:
    print(row)

print("\nHeap Sort")
print(f"Time taken is {end - start}")