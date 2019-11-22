
arr = [1,2,3,2,1,5,6,5,5,5]
list_range = len(arr)
repeated = []
for i in range (list_range):
    a = i + 1
    for b in range(a, list_range):
        if arr[i] == arr[b] and arr[i] not in repeated:
            repeated.append(arr[i])
print("Repeted item in list are" , repeated)