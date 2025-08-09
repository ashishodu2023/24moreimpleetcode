"""
Given an array of non-negative integers nums and an integer K,
Return the maximum length of a contiguous subarray whose sum is at most K.
If no such subarray exists, return 0.

nums = [1, 2, 1, 0, 1, 1, 0], K = 4  
Answer → 5   // subarray [1, 2, 1, 0, 1]

Time O(n)
Space O(1)
"""
def longest_subarray(nums:list[int],K:int)->int:
    max_len = 0 
    n = len(nums)
    current_sum = 0
    left = 0 

    if not nums:
        return 0
    
    for right in range(n):

        current_sum+=nums[right]

        while current_sum>K and left<=right:
            current_sum-=nums[left]
            left+=1

        max_len = max(max_len,right - left + 1)

    return max_len



# Example test
if __name__ == "__main__":
    test_cases = [
        # (nums, k, expected)
        ([], 5, 0),                     # empty array
        ([5, 6, 7], 4, 0),              # all elements > k
        ([0, 0, 1, 0], 0, 2),           # k = 0 with zeros
        ([1], 0, 0),                    # single element > k
        ([1], 1, 1),                    # single element ≤ k
        ([0, 0, 0], 0, 3),              # all zeros
        ([1, 2, 3], 6, 3),              # k ≥ sum(nums)
        ([1, 2, 1, 0, 1, 1, 0], 4, 5),   # provided example
    ]

    for nums, k, expected in test_cases:
        result = longest_subarray(nums, k)
        print(f"nums={nums}, k={k} -> {result} (expected {expected})")
        assert result == expected, f"Test failed for nums={nums}, k={k}"

