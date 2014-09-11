#sum_of_3_elements.py

L = [1,2,3,4,5,6,7,8,9,10]

def sum3el(L,v):
	global found
	h = len(L)//2 # half of List
	print('{} {} {}'.format(L[0],L[h],L[-1]))
	total = L[0] + L[h] + L[-1]
	print(total)

	if total == v:
		found = L
		#found = '{} + {} + {}'.format(L[0]+L[h]+L[-1])
	if total > v:
		sum3el(L[:-1],v)
	if total < v:
		sum3el(L[1:],v)

	return found

print(sum3el(L,10))



