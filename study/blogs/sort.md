
简单的排序算法-python

之前面试的时候经常被问到排序算法，每次都回答不上来，排序算法算是对算法的入门，对于排序算法想要掌握应该先掌握排序算法的思想，代码是对思想的展示，只有真正理解思想后才能真正掌握排序算法，对于其他的算法肯定也是先掌握思想
下面主要记录一下简单的排序算法，冒泡排序，选择排序，插入排序，希尔排序，归并排序，快速排序，都按照升序排列
#冒泡排序
冒泡排序是对相邻的两个进行比较，如果后者比前者小则替换位置，然后继续向后比较，这样每次都能将最大的数字排到最后，每次循环都能将最大的数字排到最后,排序过程嵌套两个for循环，时间复杂度最好时为O(n)最坏时为O(n²),平均时间复杂度为O(n²)
```base
def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(1,len(arr) - i):
			if arr[j - 1] > arr[j]:
				arr[j],arr[j - 1] = arr[j - 1],arr[j]
	return arr1
```

#选择排序
选择排序相当于从数组中选中一个最小的数值放在首位,每次循环的时候嵌套的循环默认从未排序的位置开始,时间复杂度最好时为O(n²)最坏时为O(n²),平均时间复杂度为O(n²)
```base
def slectSort(arr):
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			if arr[i] > arr[j]:
				arr[j],arr[i] = arr[i],arr[j]
	return arr
```

#插入排序
插入排序类似于打扑克牌时起牌,新起的牌会插入到前者小于自己后者大于自己的位置,手中已有重复的话可以插入同等牌的左边或者右边(根据比较时从左边比较还是右边比较),排序时先看前面是否有已排好的,如果有的话且满足最后一个数字大于新数字的话则进行位置后移,最后将新数字插入到preIndex的后一位,时间复杂度最好时为O(n)最坏时为O(n²),平均时间复杂度为O(n²)
```base
def insertSort(arr):
	for i in range(len(arr)):
		preIndex = i - 1
		current = arr[i]
		while preIndex >= 0 and arr[preIndex] > current:
			arr[preIndex + 1] = arr[preIndex]
			preIndex -= 1
		arr[preIndex + 1] = current
	return arr
```

#希尔排序
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率。
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。
希尔排序是通过一个增量将需要排序的数分成多组然后对每一组进行插入排序,这个增量一般开始的时候为数组数量的一半,最后为1,代码中3可以替换为其他的值,会影响到分组的次数,时间复杂度最好时为O(nlogn)最坏时为O(nlog²n),平均时间复杂度为O(nlog²n)
```base
import math
def shellSort(arr)
	gap = 1
	while gap < math.floor(len(arr) / 3):
		gap = gap * 3 + 1
	while gap > 0:
		for g in range(gap):
			for i in range(g, len(arr), gap):
				preIndex = i - gap
				current = arr[i]
				while preIndex >= 0 and arr[preIndex] > current:
					arr[preIndex + gap] = arr[preIndex]
					preIndex -= gap
				arr[preIndex + gap] = current
		gap = math.floor(gap / 3)
	return arr
```

#归并排序
归并排序相当于将数组先分为两组,然后将子数组再分别分为两组一直到子子...子数组里面只有一个或者0个元素为止,然后合并这些子数组一直到将数组最后合并成一个有序的数组,时间复杂度最好时为O(nlogn)最坏时为O(nlogn),平均时间复杂度为O(nlogn)
```base
def mergeSort(arr):
	if len(arr) < 2:
		return arr
	midIndex = math.floor(len(arr) / 2)
	left,right = arr[:midIndex],arr[midIndex:]
	return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
	result = []
	while left and right:
		if left > right:
			result.append(right.pop(0))
		else:
			result.append(left.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result
```

#快速排序
快速排序命名很粗暴,快速排序是对冒泡排序的一个优化,首先选择数组中的一个元素,将后面的元素数值小于这个数的放在左边,大于或者等于的放在右边,递归的对拆分出的数组进行同样的排序最后得到一个有序的数组,时间复杂度最好时为O(nlogn)最坏时为O(n²),平均时间复杂度为O(nlogn)
```base
def quickSort(arr,left,right):
	if left < right:
		partitionIndex = partition(arr,left,right)
		quickSort(arr,left,partitionIndex - 1)
		quickSort(arr,partitionIndex + 1,right)
	return arr

def partition(arr,left,right):
	provt = left
	index = left + 1
	i = index
	while i <= right:
		if arr[i] < arr[provt]:
			arr[i],arr[index] = arr[index],arr[i]
			index += 1
		i += 1
	arr[index - 1],arr[provt] = arr[provt],arr[index - 1]
	return index - 1
```




