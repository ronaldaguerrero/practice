def selection_sort(arr):
	for i in range(len(arr)):
		mIdx = i;
		for j in range(i+1,len(arr)):
			if (mIdx > arr[j]):
				mIdx = j
		arr[mIdx], arr[i] = arr[i], arr[mIdx]
		return arr

def bubble_sort