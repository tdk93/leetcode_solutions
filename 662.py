

class Solution:
    def __init__(self):
        self.minimum_vals = {}
        self.maximum_vals = {}


    def traverseTree(self,current_node,current_lvl, current_val):
        if current_node is None:
            return
        if current_lvl not in self.minimum_vals:
            self.minimum_vals[current_lvl] = current_val
        else:
            self.minimum_vals[current_lvl] = min(current_val,self.minimum_vals[current_lvl])

        if current_lvl not in self.maximum_vals:
            self.maximum_vals[current_lvl] = current_val
        else:
            self.maximum_vals[current_lvl] = max(current_val,self.maximum_vals[current_lvl])

        self.traverseTree(current_node.left, current_lvl+1, 2*(current_val-1)+1)
        self.traverseTree(current_node.right, current_lvl+1, 2*(current_val-1)+2)


    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverseTree(root,0,1)
        

        ans = 0
        for level in self.minimum_vals.keys():
            ans = max(ans, self.maximum_vals[level]-self.minimum_vals[level])
        return ans+1
