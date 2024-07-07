from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_leaf_nodes(root: Optional[TreeNode]):
    
    if not root:
        return
    
    
    if not root.left and not root.right:
        print(root.val)
        return
    
    if root.left:
        print_leaf_nodes(root.left)
    if root.right:
        print_leaf_nodes(root.right)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    print("Leaf nodes in the BST are:")
    print_leaf_nodes(root)
