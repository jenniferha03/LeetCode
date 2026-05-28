class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;

        sort(intervals.begin(), intervals.end());
        ans.push_back(intervals[0]);

        for (auto interval : intervals) {
            if (interval[0] > ans.back()[1]) {
                ans.push_back(interval);
            } else if (interval[1] > ans.back()[1]) {
                ans.back()[1] = interval[1];
            }
        }

        return ans;
    }
};