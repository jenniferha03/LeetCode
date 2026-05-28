class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        for (int i = nums.size() - 1; i >= 1; i -= 1) {
            if (nums[i] > nums[i - 1]) {
                for (int j = nums.size() - 1; j >= i; j -= 1) {
                    if (nums[j] > nums[i - 1]) {
                        swap(nums[j], nums[i - 1]);
                        sort(nums.begin() + i, nums.end());
                        return;
                    }
                }
            }
        }
        sort(nums.begin(), nums.end());

        // 4 2 3 1 6 5
        // 4 2 3 5 1 6
    }
};