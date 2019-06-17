def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if (arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
	print(arr)

bubble_sort([1,5,3,4,2])