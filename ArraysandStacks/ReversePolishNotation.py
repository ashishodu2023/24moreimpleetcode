""" 
You are given an array of strings representing a valid Reverse Polish Notation (RPN) expression. Evaluate it and return the result as an integer.

RPN Rule:

    Operands come before the operator.

    Evaluate when you see an operator.
    
    
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9

Why?  
(2 + 1) * 3 = 3 * 3 = 9

Use a stack to store numbers.

For each token:

    If it's a number, push onto the stack.

    If it's an operator, pop the last two numbers, apply the operator, push result back.

After all tokens, the result is the last item in the stack.

O(N)
"""
from collections import deque

def evalRPN(tokens:list[int]) ->int:
    
    if not tokens:
        return 0
    
    if len(tokens) ==  1:
        return tokens[0]
    
    stack = deque()
    
    for token in tokens:
        if token in "+-*/":
            num2 = stack.pop()
            num1 = stack.pop()
            
            if token == '+':
                stack.append(num1+num2)
            elif token ==  '-':
                stack.append(num1-num2)
                
            elif token ==  '*':
                stack.append(num1*num2)
                
            else:
                stack.append(int(num1/num2))
        
        else:
            stack.append(int(token))
            
            
    return stack.pop()


def main():
    tests = [
        ["2", "1", "+", "3", "*"],     # (2 + 1) * 3 = 9
        ["4", "13", "5", "/", "+"],    # 4 + (13 / 5) = 6
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ]

    for idx, tokens in enumerate(tests):
        result = evalRPN(tokens)
        print(f"Test Case {idx + 1}: Input: {tokens}")
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
                