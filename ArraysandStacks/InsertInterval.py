# https://leetcode.com/problems/insert-interval/

"""
You are given a list of non-overlapping intervals sorted by their start time. You are also given a new interval to insert into the list, 
and your job is to insert it into the correct place and merge overlapping intervals.

Example:
Input:
intervals = [[1,3], [6,9]]
newInterval = [2,5]

Output:
[[1,5], [6,9]]

Explanation:

    [1,3] overlaps with [2,5] ➔ merge them into [1,5].
    [6,9] doesn't overlap with anything.
    
    
Intuition / Steps:

    Go through each interval:

        If it ends before newInterval starts ➔ add it as-is.

        If it starts after newInterval ends ➔ add newInterval and all following intervals.

        If they overlap ➔ merge intervals.

    After merging, update newInterval to the merged range.

O(n) 
"""

def insert(intervals:list[list[int]],newInterval:list[int]) -> list[list[int]]:
    
    result =[]
    
    if not intervals:
        return [newInterval]
    
    if not newInterval:
        return intervals
    
    for interval in intervals:
    
    #Case1: When interval is completely before newInterval.Non-overlapping
        if interval[1]<newInterval[0]:
            result.append(interval)
    
    #Case2: When interval is completely after newInterval.Non-overlapping
        if interval[0]>newInterval[1]:
            result.append(newInterval)
            newInterval = interval     
    
    #Case3: Overlapping intervals, merge them 
        else:
            newInterval[0] = min(newInterval[0],interval[0])
            newInterval[1] = max(newInterval[1],interval[1])
            
            
    # Last interval after the loop
    result.append(newInterval)   
    
    return result
            
            
def main():
    # List of test cases for edge and corner cases
    tests = [
        # Typical Example
        ([[1, 3], [6, 9]], [2, 5]),
        # Corner Cases
        ([], [5, 7]),
        ([[1, 3], [6, 9]], []),
        ([[5, 7], [10, 12]], [1, 3]),
        ([[1, 2], [3, 5]], [7, 9]),
        ([[1, 2], [3, 5], [6, 7]], [0, 10]),
        ([[1, 2], [3, 5], [6, 7], [8, 10]], [4, 8]),
        ([[1, 10]], [3, 5]),
    ]

    for idx, (intervals, newInterval) in enumerate(tests):
        result = insert(intervals, newInterval)
        print(f"Test Case {idx + 1}:")
        print(f"Input intervals: {intervals}")
        print(f"New Interval: {newInterval}")
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()

