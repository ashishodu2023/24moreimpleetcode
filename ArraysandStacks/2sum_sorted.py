def two_sum_sorted(nums:list[int],target:int)->list[int]:
    
    n = len(nums)
    left = 0
    right = n - 1
    arr_sum = 0 
    
    while left<right:
        
        arr_sum = nums[left] + nums[right]
        if arr_sum == target:
            return [left,right]
        
        if arr_sum < target:
            left +=1
        else:
            right-=1
            
    return None
            

assert two_sum_sorted([1,2,3,4,6,8], 10) in ([1,5],[2,4])
assert two_sum_sorted([1,2,3], 7) is None
    
    
    



