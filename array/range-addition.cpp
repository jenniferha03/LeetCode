class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> vals(length + 1);

        for (auto update : updates) {
            vals[update[0]] += update[2];
            vals[update[1] + 1] -= update[2];
        }

        vector<int> ans;
        int s = 0;
        for (int i = 0; i < length; ++i) {
            s += vals[i];
            ans.push_back(s);
        }
        return ans;
    }
};