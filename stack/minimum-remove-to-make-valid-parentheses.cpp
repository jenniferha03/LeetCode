class Solution {
public:
    string minRemoveToMakeValid(string s) {
        string ans = "";
        int openCount = 0;
        int closeCount = 0;
        for (auto c : s) {
            if (c == ')') {
                closeCount += 1;
            }
        }

        for (auto c : s) {
            if (c == ')') {
                openCount -= 1;
                closeCount -= 1;
            }
            if (c == '(') {
                openCount += 1;
            }

            if (openCount < 0) {
                openCount = 0;
            } else if (openCount > closeCount) {
                openCount -= 1;
            } else {
                ans.push_back(c);
            }
        }

        return ans;
    }
};