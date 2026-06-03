import math

def algo1_enumeration(A):
	n = len(A)
	min_sum = float('inf')
	for i in range(n):
		for j in range(i, n):
			current_sum = sum(A[i:j+1])
			if abs(current_sum) < min_sum:
				min_sum = abs(current_sum)
	return min_sum
