import math

def algo4_dc_sort(A):
	if len(A) == 1:
		return abs(A[0])
	if len(A) == 0:
		return float('inf')

	mid = len(A) // 2
	left_min = algo4_dc_sort(A[:mid])
	right_min = algo4_dc_sort(A[mid:])
    
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
        
	combined = [(s, 'S') for s in S] + [(-p, 'P') for p in P]
	combined.sort(key=lambda x: x[0])
    
	cross_min = float('inf')
    
	last_S = None
	last_P = None
    
	for val, origin in combined:
		if origin == 'S':
			last_S = val
			if last_P is not None:
				cross_min = min(cross_min, abs(val - last_P))
		else:
			last_P = val
			if last_S is not None:
				cross_min = min(cross_min, abs(last_S - val))
                
	return min(left_min, right_min, cross_min)
