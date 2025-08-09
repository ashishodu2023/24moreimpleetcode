"""
Given a string s, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.

Expand the window by moving right pointer.
If you see a duplicate character, shrink the window from the left until the duplicate is removed.
Use a set to keep track of characters in the current window.
""" 

def lengthOfLongestSubstring(s:str)->int:
    
    if not s:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window if duplicate is found
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
            
        # Expand window to the right
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length    
        


def main():
    test_cases = [
        ("", 0),
        (" ", 1),
        ("bbbbbbb", 1),
        ("abcdef", 6),
        ("abba", 2),
        ("pwwkew", 3),
        ("tmmzuxt", 5)
    ]

    for idx, (s, expected) in enumerate(test_cases):
        result = lengthOfLongestSubstring(s)
        print(f"Test Case {idx+1}: Input: '{s}' | Expected: {expected} | Got: {result}")


if __name__ == "__main__":
    main()