def selection_sort(arr):
	for i in range(len(arr)):
		mIdx = i
		for j in range(i, len(arr)):
			if(arr[mIdx] > arr[j]):
				mIdx = j
		print('before')
		print(arr)
		arr[mIdx], arr[i] = arr[i], arr[mIdx]
		print('after')
		print(arr)
	print(arr)

selection_sort([5,3,2,1,4])