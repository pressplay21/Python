#list_sliding_window.py

#Given a window size, find the max number of the window
#slide by 3 elements
#max([2,3,6]) = 6
#max([3,6,2]) = 6
#max([6,2,9]) = 9
#max([2,9,10]) = 10

L = [2,3,6,2,9,10]

def slide(data,window=3):
	length = len(data)
	first = 0
	last = window
	while length:
		length = len(L[first:last])
		if length < window:
			break
		M = L[first:last]
		result = max(M)
		print(result)
		first +=1
		last +=1

slide(L,3)