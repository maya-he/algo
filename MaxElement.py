def MaxElement(arr):  
    maxval = arr[0] 
    for i in range(1,len(arr)):

        if arr[i] > maxval:

            maxval = arr[i]

    return maxval

arr = [1,2,3,4,5,6]
print(MaxElement(arr))