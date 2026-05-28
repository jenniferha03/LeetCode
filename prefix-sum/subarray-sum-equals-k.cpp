class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        int s = 0;
        int ans = 0;
        m[s] = 1;

        for (auto num : nums) {
            s += num;
            if (m.find(s - k) != m.end()) {
                ans += m[s-k];
            }
            if (m.find(s) == m.end()) {
                m[s] = 0;
            }
            m[s] += 1;
        }

        return ans;
    }
};