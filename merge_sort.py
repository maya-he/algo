arr = [5,2,1,7,8,9]

def merge(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge(left_arr)
        merge(right_arr)

        i = 0  #left arr idx
        j = 0  #right arr idx
        k = 0  #merged arr idx

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1 
            else:
                arr[k] = right_arr[j]
                j += 1
            k +=1 

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1

merge(arr)
print(arr)