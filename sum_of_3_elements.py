#sum_of_3_elements.py

#Given a number. 
#Find the sum of 3 elements in a list which equals the number.
#sorting O(n log n)
#finding third elements O(n)
#finding two elements O(n^2)

L = [-4,-3,-5,1,3,4,5,0,9,6,-2]


def findSumOf3(data,target,sort=1):
	global result
	result = False
	length = len(data)
	if data == None or length < 3:
		return result
	if sort:
		data = sorted(data) #if sorting is needed
	for i in range(0,length-1):
		value = data[i] #third element at each iteration
		result = findSumOf2(data,value,i,target) #send the third element to sum with two other elements
		if result:
			break
	return result if result else False

def findSumOf2(data,value,index,target=0):
	global result
	result = False
	length = len(data)
	first = 0
	last = length-1
	while last > first: 
		if first == index: #skip ith element
			first += 1
		if last == index: #skip ith element
			last -= 1
		#add third element + two elements
		total = value + data[first] + data[last]
		if total == target:
			print('L[{}]:{} L[{}]:{} L[{}]:{}'.format(index,data[index],first,data[first],last,data[last]))
			result = True
			break
		elif total > target: #scan backward if total is bigger than target
			last -= 1
		else:
			first +=1 #scan forward if total is less than target
	return result if result else False

print(findSumOf3(L,0))
print('-'*30)
print(findSumOf3(L,19))
print('-'*30)
print(findSumOf3(L,45))
