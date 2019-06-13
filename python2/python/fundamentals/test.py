# def bubble_sort(arr):
# 	for i in range(len(arr)):		
# 		for j in range(len(arr)-1-i):
# 			if(arr[j] > arr[j+1]):
# 				arr[j], arr[j+1] = arr[j+1], arr[j]
# 	print(arr)
	
# bubble_sort([5,3,2,1,4])

# def selection_sort(arr):

def insertion_sort(arr):
	for i in range(len(arr)):
		j = i - 1
		iVal = arr[i]
		while(j > 0 and iVal > arr[j]):
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = iVal
	print(arr)

insertion_sort([5,3,2,1,4])

s