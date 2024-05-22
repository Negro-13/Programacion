listdes = [4, 3, 2, 1, 5, 6]
min = []
max = []
k = 4
def partList(listdes, k):
    for num in listdes:
        if num < k:
            min.append(num)
        else:
            max.append(num)
    return min + max
print(partList(listdes, k))