class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None
class Traversal(object):
    def __init__(self):
        self.traverse_path = list()
    def preorder(self,root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
        