""" 
Given an integer array nums, return an array answer such that:

    answer[i] is the product of all elements of nums except nums[i].

    Do not use division.

    Solve it in O(N) time.

Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Two Passes:

1 First pass (Left Product):

    For every index i, store product of elements to the left of i.

2 Second pass (Right Product):

    For every index i, multiply it by the product of elements to the right of i.
O(n)  
"""

def productExceptSelf(nums:list[int])->list[int]:
    
    if not nums:
        return []
    
    if len(nums) ==1:
        return [1]
    
    n = len(nums)
    result = [1] * n
    
    # First pass: Compute products of element to the left
    
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
        
    
    #Second Pass: Compute products of the element to the right
    
    right_product = 1
    for i in reversed(range(n)):
        result[i] *= right_product
        right_product *= nums[i]
        
    
    return result
        
def main():      
    # Sample tests, including corner cases
    tests = [
        [1, 2, 3, 4],
        [],
        [5],
        [0, 4, 5],
        [1, 1, 1, 1],
        [2, 3, 0, 4],
    ]

    for idx, nums in enumerate(tests):
        result = productExceptSelf(nums)
        print(f"Test Case {idx + 1}: Input: {nums} => Output: {result}")


if __name__ == "__main__":
    main()
