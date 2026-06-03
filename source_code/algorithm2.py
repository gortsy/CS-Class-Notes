import math

def algo2_better_enumeration(A):
	n = len(A)
	min_sum = float('inf')
	for i in range(n):
		current_sum = 0
		for j in range(i, n):
			current_sum += A[j]
			if abs(current_sum) < min_sum:
				min_sum = abs(current_sum)
	return min_sum
