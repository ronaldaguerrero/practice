arr = [5,3,6,2,1]

def selectionsort(arr):
	for i in range(len(arr)):
		# print('this is i', i)

		for j in range(i+1, len(arr)):
			if arr[i] > arr[j]:
				print('this is j', arr[j])

				temp = arr[i]
				print('this is the value of temp', arr[i])
				
				arr[i] = arr[j]
				print('arr[i] is being changed to arr[j]', arr[j])
				
				arr[j] = temp
				print('arr[j] is being changed to temp')
				
				print(arr)

	return arr

selectionsort(arr);
		