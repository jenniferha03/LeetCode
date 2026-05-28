/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        if (p != nullptr) {
            if (visited.find(p->val) != visited.end()) return visited[p->val];
            visited[p->val] = p;
            p = p->parent;
        }
        if (q != nullptr) {
            if (visited.find(q->val) != visited.end()) return visited[q->val];
            visited[q->val] = q;
            q = q->parent;
        }
        return lowestCommonAncestor(p, q);
    }

private:
    unordered_map<int, Node*> visited;
};