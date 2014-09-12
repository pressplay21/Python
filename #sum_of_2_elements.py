#sum_of_2_elements.py


#Sum of 2 elements = 15
#Array is increasingly sorted
L = [1,2,3,4,5,7,9,12,15,18,20]

def sum2el(L,t):
	global found
	found = None	
	if len(L) >= 2: #need at least two elements
		first,last = L[0],L[-1]
		total = first + last
		if total == t:
			 found = '{} + {}'.format(L[0],L[-1])
		elif total > t:
			sum2el(L[:-1],t) #if total is bigger than target, pop out the last element
		elif total < t:
				sum2el(L[1:],t) #if total is smaller than target, pop out the first element	
	if found:
		return found
	else:
		return "No Solution"

print(sum2el(L,32))
