"""
Given an array of positive integers nums and an integer k,
Return the minimal length of a contiguous subarray of which the sum is at least k.
If no such subarray exists, return 0.

Example:
    nums = [2, 3, 1, 2, 4, 3], k = 7
    Answer → 2   # subarray [4, 3]

"""

def min_subarray(nums: list[int], k: int) -> int:
    # Corner cases
    if not nums or k <= 0:
        return 0

    n = len(nums)
    left = 0
    current_sum = 0
    min_len = n + 1

    for right, val in enumerate(nums):
        current_sum += val
        # shrink from the left while we meet the target
        while current_sum >= k:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len <= n else 0


if __name__ == "__main__":
    test_cases = [
        ([],  7, 0),   # empty
        ([1,2,3], 0, 0),  # k <= 0
        ([5], 5, 1),      # exact match
        ([5], 6, 0),      # below k
        ([2,3,1,2,4,3], 7, 2),  # example
        ([1,2,3,4,5], 11, 3),   # corrected: [3,4,5]
        ([1,2,3,4,5], 16, 0),   # total sum < k
        ([1,1,1,1], 2, 2),      # smallest window of size 2
    ]

    for nums, k, expected in test_cases:
        result = min_subarray(nums, k)
        print(f"nums={nums}, k={k} -> {result} (expected {expected})")
        assert result == expected