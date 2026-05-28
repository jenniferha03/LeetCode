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
    int maxPathSum(TreeNode* root) {
        return dfs(root).first;
    }

private:
    // dfs return pair of max path sum and max path sum ends at node.
    pair<int, int> dfs(TreeNode *node) {
        if (node == nullptr) {
            return {INT_MIN, 0};
        }

        auto l = dfs(node->left);
        auto r = dfs(node->right);
        int newSum = max(l.second, 0) + max(r.second, 0) + node->val;
        return {
            max(newSum, max(r.first, l.first)),
            max(0, max(l.second, r.second)) + node->val
        };
    }
};