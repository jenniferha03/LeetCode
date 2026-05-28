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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> left = {{}};
        vector<vector<int>> right;
        traverse(root, left, right);

        vector<vector<int>> ans;
        for (int i = left.size() - 1; i >= 1; --i) ans.push_back(left[i]);
        for (auto r : right) ans.push_back(r);
        return ans;
    }

private:
    void traverse(
        TreeNode* root,
        vector<vector<int>> &left,
        vector<vector<int>> &right
    ) {
        queue<pair<int, TreeNode*>> q;
        q.push({0, root});

        while (!q.empty()) {
            pair<int, TreeNode*> nodeData = q.front();
            q.pop();

            int id = nodeData.first;
            if (nodeData.second == nullptr) continue;
            if (id < 0) {
                if (left.size() <= -id) left.push_back({});
                left[-id].push_back(nodeData.second->val);
            } else {
                if (right.size() <= id) right.push_back({});
                right[id].push_back(nodeData.second->val);
            }

            q.push({id - 1, nodeData.second->left});
            q.push({id + 1, nodeData.second->right});
        }
    }
};