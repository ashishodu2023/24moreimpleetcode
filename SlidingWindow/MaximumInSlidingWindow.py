""" 
Given:
An array nums and a window size k.
Find:
The maximum element in each sliding window of size k.

Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]

    "What’s the max in this current window?" — in O(1) time.

How? Use a deque to store indices.
Keep deque decreasing:

    The front will always have the index of the maximum element in the current window.

    Remove indices from the back if they are smaller than the current number (nums[i]).

    Remove indices from the front if they are outside the current window.
    
"""
from collections import deque

def maxSlidingWindow(nums:list[list], k:int) -> list[int]:
    
    if not nums:
        return []
    
    result = []
    queue = deque() #Store indiecs not values
    
    for i in range(len(nums)):
        
        #1 Remove ouf of window indicies
        if queue and queue[0]<i -k + 1:
            queue.popleft()

        #2 Maintain decreasing order in deque
        while queue and nums[i]>=nums[queue[-1]]:
            queue.pop()
            
        # Add current index    
        queue.append(i)
        
        
        #Collect max when slidign window is fully ready
        if i>= k - 1:
            result.append(nums[queue[0]]) # The front is the max
            
            
    return result

def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = maxSlidingWindow(nums, k)
    print("Maximum in each sliding window:", result)


if __name__ == "__main__":
    main()
