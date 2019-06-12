def bubblesort(arr): #swap pairs
    for i in range(len(arr)): # start at beginning and loop to end
        for j in range(len(arr)-1-i): # start at beginning and loop to end minus 'i' because the largest # is at the end
            if arr[j]>arr[j+1]: # if current is larger then next
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    return arr

arr = [54,26,93,17,77]
bubblesort(arr)
print(arr)
