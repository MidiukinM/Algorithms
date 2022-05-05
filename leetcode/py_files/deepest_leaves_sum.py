# given the root of a binary tree, return the sum of values of its deepest leaves

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepest_leaves_sum(self, root: TreeNode) -> int:
        pass


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    print(Solution().deepest_leaves_sum(root))