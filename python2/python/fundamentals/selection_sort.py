def selection_sort(arr):
    for i in range(len(arr)): # first loop
        m_idx = i # set min index
        for j in range(i+1, len(arr)): # second loop starting at i + 1
            if(arr[j] < arr[m_idx]): # search for lowest val
                m_idx = j # set min index for lowest val
        arr[i], arr[m_idx] = arr[m_idx], arr[i] # preform swap outside of loop
    print(arr)
    return arr
    
selection_sort([5,4,2,1,3])