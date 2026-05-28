class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int ans = 0;
        prices.push_back(-1);
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] < prices[i - 1]) {
                if (i - 1 != l) {
                    ans += prices[i - 1] - prices[l];
                }
                l = i;
            }
        }

        return ans;
    }
};