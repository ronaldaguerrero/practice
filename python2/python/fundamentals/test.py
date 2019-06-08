def selection_sort(arr):
	for i in range(len(arr)):
		mIdx = i
		for j in range(i, len(arr)): # i+1 !!!!
			if (arr[mIdx] > arr[j]):
				mIdx = j
		arr[mIdx], arr[i] = arr[i], arr[mIdx]
	print (arr)