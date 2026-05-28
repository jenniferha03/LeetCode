class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> minR(nums.size() + 1, INT_MAX);

        for (int i = nums.size() - 1; i >= 0; --i) {
            minR[i] = min(minR[i + 1], nums[i]);
        }

        int maxL = nums[0];
        int fPos = INT_MAX;
        int lPos = -1;
        for (int i = 0; i < nums.size(); ++i) {
            cout << fPos << " " << lPos << "\n";
            if (maxL > nums[i]) {
                lPos = i;
            }
            if (nums[i] > minR[i]) {
                fPos = min(fPos, i);
            }
            maxL = max(maxL, nums[i]);
        }

        if (fPos == INT_MAX) return 0;
        return lPos - fPos + 1;
    }
};