arr = [5,3,6,2,1]

def selectionsort(arr):
	# loop through
	for i in range(len(arr)):
		# loop again
		for j in range(i+1, len(arr)):
			# check if i is greater than j
			if arr[i] > arr[j]:
				# swap
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
				print(arr)

	return arr

selectionsort(arr);
		