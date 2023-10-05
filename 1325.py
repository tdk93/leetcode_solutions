# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeSubtrees(self, node:Optional[TreeNode], target:int)-> bool:
        if node == None:
            return True
        
        lv = self.removeSubtrees(node.left,target)
        rv = self.removeSubtrees(node.right,target)

        if lv:
            node.left = None
        if rv:
            node.right = None
        
        if lv and rv and node.val == target:
            return True
        return False
    
    
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root==None:
            return root
        
        self.removeSubtrees(root,target)
        if root.left == None and root.right== None and root.val == target:
            return None
        
        return root


    
