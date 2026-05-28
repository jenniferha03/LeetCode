/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        traverse(root, 0, ans);
        return ans;
    }

private:
    void traverse(TreeNode *node, int h, vector<int> &ans) {
        if (node == nullptr) return;
        
        if (h == ans.size()) ans.push_back(0);
        ans[h] = node->val;
        traverse(node->left, h + 1, ans);
        traverse(node->right, h + 1, ans);
    }
};