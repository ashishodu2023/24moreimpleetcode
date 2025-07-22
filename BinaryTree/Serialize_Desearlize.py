from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Iterative serialize
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "#"
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(str(node.val))
                # Push right first so left is processed first
                stack.append(node.right)
                stack.append(node.left)
            else:
                result.append("#")
        return ','.join(result)

    # Iterative deserialize
    def deserialize(self, data: str) -> TreeNode:
        if data == "#":
            return None

        nodes = deque(data.split(","))
        root_val = nodes.popleft()
        root = TreeNode(int(root_val))
        stack = [(root, False)]  # (node, is_right_child)

        while nodes:
            val = nodes.popleft()
            parent, is_right = stack.pop()

            if val != "#":
                child = TreeNode(int(val))
                if not is_right:
                    parent.left = child
                else:
                    parent.right = child
                # Push right first, then left
                stack.append((parent, True))  # Now need to assign right child
                stack.append((child, False))
            else:
                if not is_right:
                    stack.append((parent, True))  # Right child next

        return root


def printPreorder(root):
    if not root:
        return
    print(root.val, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)


def main():
    # Tree: 1 -> (2, 3) -> (None, None, 4, 5)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    serialized = codec.serialize(root)
    print("Serialized Tree (Iterative DFS):", serialized)

    deserialized = codec.deserialize(serialized)
    print("Preorder of Deserialized Tree:")
    printPreorder(deserialized)
    print()


if __name__ == "__main__":
    main()
