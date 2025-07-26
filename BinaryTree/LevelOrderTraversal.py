from collections import deque


class TreeNode:

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right


def bfs_level_order_traversal(root):

    queue = deque([root])
    result = []

    if not root:
        return []

    while queue:
        level_result = []
        for _ in range(len(queue)):

            node = queue.popleft()
            level_result.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        result.append(level_result)

    return result


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
    print("Level Order Traversal:  ", bfs_level_order_traversal(root))


if __name__ == "__main__":
    main()
