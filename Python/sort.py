#http://www.runoob.com/python3/python3-tutorial.html

import time;



arr = [77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35]

arr2 = [77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35,77,1,3,57,3,67,9,0,8,7,54,24,4,7,78,89,23,22,56,89,34,35]

#冒泡排序
def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(1,len(arr)-i):
			if arr[j-1] > arr[j]:
				arr[j-1],arr[j] = arr[j],arr[j-1]
	return arr


#选择排序
def selecteSort(arr):	
	for i in range(len(arr)):
		minIndex = i
		for j in range(i,len(arr)):
			if arr[minIndex] > arr[j]:
				minIndex = j
		arr[i],arr[minIndex] = arr[minIndex],arr[i]
	return arr

#选择排序与冒泡排序结合
def selectionSort(arr):
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[j] < arr[i]:
				arr[j],arr[i] = arr[i],arr[j]
	return arr




#插入排序
def insertionSort(arr):
	for i in range(len(arr)):
		preIndex = i - 1
		current = arr[i]
		while preIndex >= 0 and arr[preIndex] > current:
			arr[preIndex + 1] = arr[preIndex]
			preIndex -= 1
		arr[preIndex + 1] = current
	return arr

#希尔排序shellSort比shellSort2用时更少一些，用时比例约为0.82:1.00
import math
def shellSort(arr,step):
    gap = 1
    while gap < len(arr) / step:
    	gap = gap * step + 1
    while gap > 0:
    	for s in range(gap):
    		for i in range(s,len(arr),gap):
    			j = i - gap
    			current = arr[i]
    			while j >= 0 and arr[j] > current:
    				arr[j + gap] = arr[j]
    				j -= gap
    			arr[j + gap] = current
    	gap = math.floor(gap/step)    	
    return arr
#希尔排序
def shellSort2(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr
 
#归并排序
def mergeSort(arr):
	if len(arr) < 2:
		return arr
	middle = math.floor(len(arr)/2)
	left,right = arr[:middle],arr[middle:]
	return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
	result = []
	while left and right:
		if left[0] > right[0]:
			result.append(right.pop(0))
		else:
			result.append(left.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result

#快速排序
def quickSort(arr,left,right):
	left = 0 if not isinstance(left,(int,float)) else left
	right = len(arr)-1 if not isinstance(right,(int,float)) else right
	if left < right:
		partitionIndex = partition(arr,left,right)
		quickSort(arr,left,partitionIndex-1)
		quickSort(arr,partitionIndex+1,right)
	return arr

def partition(arr,left,right):
	pivot = left
	index = pivot + 1
	i = index
	while i <= right:
		if arr[i] < arr[pivot]:
			arr[i],arr[index] = arr[index],arr[i]
			index += 1
		i += 1
	arr[pivot],arr[index-1] = arr[index-1],arr[pivot]
	return index-1
	



# print(time.time())
# sortArr = bubbleSort(arr)
# sortArr = selecteSort(arr)
# sortArr = selectionSort(arr)
# sortArr = insertionSort(arr)
# sortArr = shellSort(arr,3)
# sortArr = shellSort(arr)
# sortArr = mergeSort(arr)
sortArr = quickSort(arr,0,len(arr)-1)
# print(time.time())
print(sortArr)


# print(time.time())
# shellSort2(arr)
# print(time.time())

# print(time.time())
# shellSort(arr,3)
# print(time.time())




