"""
Given an array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

    i != j != k
    nums[i] + nums[j] + nums[k] == 0


Sort the array.

For every index i from 0 to len(nums) - 2:

    If i > 0 and nums[i] == nums[i - 1]: skip duplicates.
    Set left = i + 1, right = len(nums) - 1
    While left < right:
        Compute total = nums[i] + nums[left] + nums[right]
        If total < 0: left += 1.
        If total > 0: right -= 1.
        If total == 0: add the triplet.
            Skip duplicates for left and right.
            
O(nlogn)
"""


def threesum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        # Skip duplicate elements for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    result = threesum(nums)
    print("Unique triplets that sum to zero:", result)


if __name__ == "__main__":
    main()
