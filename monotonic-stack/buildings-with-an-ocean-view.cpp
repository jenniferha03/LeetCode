class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int highest = 0;
        vector<int> ans;

        for (int i = heights.size() - 1; i >= 0; i -= 1) {
            if (heights[i] > highest) {
                ans.push_back(i);
                highest = heights[i];
            }
        }

        sort(ans.begin(), ans.end());
        return ans;
    }
};