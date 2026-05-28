class Solution {
public:
    bool check(const vector<int> &nums, int x, int y, long long expected) {
        long long actual = 0;

        for (auto num : nums) {
            if (num > 1LL * y * expected) {
                long long extra = num - y * expected;
                actual += (extra + x - y - 1) / (x - y);
            }
        }

        return actual <= expected;
    }

    int minOperations(vector<int>& nums, int x, int y) {
        long long l = 0, r = 1e9;

        while (l <= r) {
            int mid = (l + r) / 2;
            bool ch = check(nums, x, y, mid);
            if (ch) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return r + 1;
    }
};