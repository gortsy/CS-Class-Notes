import math

def algo3_dc_enumeration(A):
	if len(A) == 1:
		return abs(A[0])
	if len(A) == 0:
		return float('inf')

	mid = len(A) // 2
	left_min = algo3_dc_enumeration(A[:mid])
	right_min = algo3_dc_enumeration(A[mid:])

	S = []
	current_suffix = 0
	for i in range(mid - 1, -1, -1):
		current_suffix += A[i]
		S.append(current_suffix)

	P = []
	current_prefix = 0
	for i in range(mid, len(A)):
		current_prefix += A[i]
		P.append(current_prefix)

	cross_min = float('inf')
	for s in S:
		for p in P:
			if abs(s + p) < cross_min:
				cross_min = abs(s + p)

	return min(left_min, right_min, cross_min)
