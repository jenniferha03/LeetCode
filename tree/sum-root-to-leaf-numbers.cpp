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
    int sumNumbers(TreeNode* root, int curNum = 0) {
        if (root == nullptr) return 0;

        curNum = curNum * 10 + root->val;
        if (root->left == nullptr && root->right == nullptr) {
            return curNum;
        }

        return sumNumbers(root->left, curNum) + sumNumbers(root->right, curNum);
    }
};