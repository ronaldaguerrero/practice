arr = [5,3,6,2,1]

def bubblesort(arr):
	for i in range(len(arr)):

		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				min = arr[j]
				print('this is min', min)
				print(arr)
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp

	return arr

bubblesort(arr);
		