def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1): # start at end and loop to beginning
        for j in range(i):
            if arr[j]>arr[j+1]: # if current is larger then next
                temp = arr[j] # swap: 
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [54,26,93,17,77,31,44,55,20]
bubbleSort(arr)
print(arr)