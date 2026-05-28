class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double curSum = 0;
        double ans = INT_MIN;

        for (int i = 0; i < nums.size(); ++i) {
            if (i < k) {
                curSum += nums[i];
                if (i == k - 1) {
                    ans = curSum / k;
                }
            } else {
                curSum = curSum - nums[i - k] + nums[i];
                ans = max(ans, curSum / k);
            }
        }

        return ans;
    }
};