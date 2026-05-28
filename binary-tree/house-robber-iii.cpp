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
    int rob(TreeNode* root) {
        auto ans = dfs(root);
        return max(ans.first, ans.second);
    }

    // return {max amount robbed including node->val, max amount robbed without node-val}
    pair<int, int> dfs(TreeNode *node) {
        if (node == nullptr) {
            return {0, 0};
        }

        auto l = dfs(node->left);
        auto r = dfs(node->right);
        return {node->val + l.second + r.second, max(l.first, l.second) + max(r.first, r.second)};
    }
};