def UniqueElements(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return False
    return True

arr = [1,2,3,4,3,6,7]
print(UniqueElements(arr))