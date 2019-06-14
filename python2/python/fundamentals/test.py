def selection_sort(arr):
	for i in range(len(arr)):
		mIdx = i
		for j in range(i+1, len(arr)):
			if (arr[mIdx] > arr[j]):
				mIdx = j
		arr[mIdx], arr[i] = arr[i], arr[mIdx]
		print(arr)

selection_sort([5,3,2,1,4])