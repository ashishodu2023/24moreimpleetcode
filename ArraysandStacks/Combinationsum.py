"""
Given a list of candidates (positive integers) and a target, return all unique combinations where:

    The candidate numbers sum to the target.

    You can reuse the same number as many times as you want.

    Answer should not contain duplicate combinations.  
    
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

This is a classic backtracking problem.
We try:

    For each number, either choose it or skip it.

    If we choose, we stay on the same index (because repetition is allowed).

    If we skip, move to the next index
    
target = 7, candidates = [2, 3, 6, 7]

Start with 2:
[2] -> [2, 2] -> [2, 2, 2] -> [2, 2, 3] (valid)
...
Start with 7:
[7] (valid)

"""

"""
General Backtracking Pattern

def backtrack(path, choices):
    if is_solution(path):
        result.append(path.copy())
        return
    
    for choice in choices:
        path.append(choice)  # Make choice
        backtrack(path, choices)  # Explore further
        path.pop()  # Undo choice (backtrack)
"""

def combinationSum(candidates:list[int], target:int) -> list[list[int]]:
    
   # Corner case 1: Empty candidates
    if not candidates:
        return []

    # Corner case 2: Target is 0
    if target == 0:
        return [[]]
    
    result = []
    
    def backtracking(start:int, path:list[int],total:int):
        
        # Base case: Found Valid Combination
        
        if total == target:
            result.append(path.copy())
            return 
        
        # Exceeds Target
        if total>target:
            return 
        
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtracking(i, path,total+candidates[i])  # Can reuse same number
            path.pop() #Backtracking
    
    backtracking(0,[],0)
    
    return result

def main():
    tests = [
        ([], 7),
        ([7], 7),
        ([9], 7),
        ([2, 4], 7),
        ([1, 2], 3),
        ([2, 3, 6, 7], 7),
        ([2, 3, 2], 7),
        ([2], 8),
        ([2, 3], 0)
    ]

    for idx, (candidates, target) in enumerate(tests):
        result = combinationSum(candidates, target)
        print(f"Test Case {idx + 1}: Candidates: {candidates}, Target: {target}")
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
    
    
