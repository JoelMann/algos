import csv

with open('randomints.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    data = data[0]
    for index, point in enumerate(data):
        data[index] = int(point)

print(data)


def insertionSorter(arr_to_sort: list) -> list:
    for i in range(1,len(arr_to_sort)):
        val = arr_to_sort[i]
        j = 0
        while j < i:
            if arr_to_sort[i]<arr_to_sort[j]:
                arr_to_sort.insert(j,arr_to_sort.pop(i))
            j+=1


    return arr_to_sort

print(insertionSorter(data))
