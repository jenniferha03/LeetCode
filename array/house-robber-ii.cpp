class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        return max(myRob(nums, 0, nums.size() - 2), myRob(nums, 1, nums.size() - 1));
    }

private:
    int myRob(const vector<int> &nums, int l, int r) {
        // dp[i] = maximum money robbed houses 1 -> i
        // dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        vector<int> dp(nums.size());
        dp[l] = nums[l];
        if (nums.size() > l + 1) {
            dp[l + 1] = max(nums[l], nums[l + 1]);
        }

        for (int i = l + 2; i <= r; ++i) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }

        return dp[r];
    }
};