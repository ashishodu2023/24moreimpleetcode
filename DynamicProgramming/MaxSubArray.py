"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

    Maintain two variables:

        Current Subarray Sum (current_sum)

        Global Maximum (max_sum)

At each position:

    Either start a new subarray from nums[i] or extend the previous subarray.

    Pick whichever gives a bigger sum.

    Update max_sum as we go.

O(N)
"""


def maxSubArray(nums: list[int]) -> int:

    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:

        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maxSubArray(nums)
    print("Maximum Subarray Sum:", result)


if __name__ == "__main__":
    main()
