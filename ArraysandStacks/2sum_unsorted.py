def two_sum(nums:list[int],target:int)->list[int]:
    if not nums:
        return []
    
    seen = {}
    for key, value in enumerate(nums):
        balance = target - value
        if balance in seen:
            return [seen[balance],key]
        seen[value] = key
        
    return None


assert two_sum([2,7,11,15], 9) in ([0,1],)
assert two_sum([3,2,4], 6) in ([1,2],)
assert two_sum([3,3], 6) in ([0,1],)
assert two_sum([1,2,3], 7) is None




