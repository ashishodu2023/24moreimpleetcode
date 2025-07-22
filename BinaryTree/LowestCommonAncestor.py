""" 
Given a binary tree, and two nodes p and q, find their Lowest Common Ancestor (LCA).
The LCA of p and q is the lowest node in the tree that has both p and q as descendants. (A node can be its own ancestor.)

        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

For p = 5 and q = 1, LCA = 3
For p = 5 and q = 4, LCA = 5

Recur down the tree from the root.

If the current node is p or q, return it.

If both left and right return non-null, current node is LCA.

If only one side returns non-null, pass that up.
O(N)
O(H) --height of tree
"""


class TreeNode:

    def __init__(self, value=0, left=None, right=None):

        self.val = value
        self.left = left
        self.right = right


def LCA(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    if not root or root == p or root == q:
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def main():
    # Construct the tree manually
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node with val 5
    q = root.right # Node with val 1

    lca = LCA(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}")

    # Test another case
    p = root.left           # Node 5
    q = root.left.right.right  # Node 4
    lca = LCA(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}")


if __name__ == "__main__":
    main()