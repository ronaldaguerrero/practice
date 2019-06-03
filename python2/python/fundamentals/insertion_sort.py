# Function to do insertion sort 
def insertionSort(arr): 
    # Loop through 1 to len(arr) 
    for i in range(1, len(arr)): 
        iVal = arr[i] 
        # Move elements of arr[0..i-1], that are greater than iVal, to one position ahead of their current position 
        j = i-1
        while j >=0 and iVal < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = iVal

arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print(arr) 