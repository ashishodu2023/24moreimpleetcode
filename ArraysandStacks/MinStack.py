"""
Design a stack that supports:

    push(x)

    pop()

    top()

    getMin() — retrieve the minimum element in constant O(1) time.

Maintain two stacks:

    Main stack: for all values.

    Min stack: for the current minimum at every push.

When pushing a number, update the min stack with the smaller between the new number and the current min.

When popping, pop both stacks.

O(1)

"""

from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)

        else:
            # Always store the current min
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("Current Min:", minStack.getMin())  # -3
    minStack.pop()
    print("Current Top:", minStack.top())  # 0
    print("Current Min:", minStack.getMin())  # -2


if __name__ == "__main__":
    main()
