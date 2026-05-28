class Solution {
public:
    int rob(vector<int>& nums) {
        // dp[i] = maximum money robbed houses 1 -> i
        // dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        if (nums.size() > 1) {
            dp[1] = max(nums[0], nums[1]);
        }

        for (int i = 2; i < nums.size(); ++i) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }

        return dp[nums.size() - 1];
    }
};