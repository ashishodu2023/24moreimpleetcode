from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs_preorder(root):  # Root Left Right

    if not root:
        return []

    result = []
    stack = deque([root])

    while stack:

        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)  # Right pushed first

        if node.left:
            stack.append(node.left)  # Left on top

    return result


def dfs_inorder(root):  # Left Root Right

    if not root:
        return []

    result = []
    stack = deque()

    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)

        current = current.right

    return result


def dfs_postorder(root):  # Left Right Root
    
    if not root:
        return []
    
    stack = deque([root])
    result = deque()
    
    while stack:
        node = stack.pop()
        result.appendleft(node.value) #Reverse order insertion.
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
    return list(result)  # Reverse the result for postorder

def build_sample_tree():
    # Tree:
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    return root


def main():
    root = build_sample_tree()
    print("Preorder:  ", dfs_preorder(root))  # [1, 2, 4, 5, 3]
    print("Inorder:   ", dfs_inorder(root))  # [4, 2, 5, 1, 3]
    print("Postorder: ", dfs_postorder(root)) # [4, 5, 2, 3, 1]


if __name__ == "__main__":
    main()
