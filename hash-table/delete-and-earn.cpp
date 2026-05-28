class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        // New nums vector where nums[i] = <value, isDependent>
        // value: possible value that could be earned
        // isDependent: if choose this value, cannot choose nums[i-1]
        vector<pair<int, bool>> newNums;

        sort(nums.begin(), nums.end());
        int i = 0;
        int prevNum = -1;
        while (i < nums.size()) {
            int curVal = nums[i];
            while (i < nums.size() - 1 && nums[i] == nums[i + 1]) {
                i += 1;
                curVal += nums[i];
            }
            if (nums[i] == prevNum + 1) {
                newNums.push_back({curVal, true});
            } else {
                newNums.push_back({curVal, false});
            }

            prevNum = nums[i];
            i += 1;
        }

        // dp[i] = max value at newNums[i]
        vector<int> dp(newNums.size());

        dp[0] = newNums[0].first;
        if (newNums.size() > 1) {
            if (newNums[1].second) {
                dp[1] = max(newNums[1].first, dp[0]);
            } else {
                dp[1] = newNums[1].first + dp[0];
            }
        }
    
        for (int i = 2; i < newNums.size(); ++i) {
            if (newNums[i].second) {
                dp[i] = max(dp[i - 2] + newNums[i].first, dp[i - 1]);
            } else {
                dp[i] = max(dp[i - 2], dp[i - 1]) + newNums[i].first;
            }
        }

        return dp[newNums.size() - 1];
    }
};