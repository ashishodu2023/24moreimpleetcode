def subarray_sum_equals_k(nums:list,k:int)->int:
    
    count = 0 
    running = 0 
    frequency = {0:1}  # prefix sum 0 seen once (empty prefix)
    
    for x in nums:
        running+=x
        count += frequency.get(running -k , 0)
        frequency[running] = frequency.get(running,0) +1 
        
        
    return count

# quick checks
assert subarray_sum_equals_k([1,1,1], 2) == 2
assert subarray_sum_equals_k([1,2,3], 3) == 2   # [1,2], [3]
assert subarray_sum_equals_k([1,-1,0], 0) == 3  # [1,-1], [0], [1,-1,0]
assert subarray_sum_equals_k([], 0) == 0
    