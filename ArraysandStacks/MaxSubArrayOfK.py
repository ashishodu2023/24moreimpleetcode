""" 
Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.


Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5, 1, 3] has the maximum sum = 9.
 
Maintain a window of size k.
Keep track of the current sum of the window.
Slide the window by:
    Add the new element at the right.
    Remove the leftmost element (shrinks window back to k size).
Keep updating the maximum sum.
"""


def maxSumSubarray(nums, k):
    window_start = 0
    window_sum = 0
    max_sum = float('-inf')  # Start with the smallest possible number
    
    for window_end in range(len(nums)):
        window_sum += nums[window_end]  # Expand the window
        
        # Once we hit the window size k
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]  # Shrink from the left
            window_start += 1

    return max_sum


def main():
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    result = maxSumSubarray(nums, k)
    print("Maximum Sum Subarray of Size K:", result)


if __name__ == "__main__":
    main()
