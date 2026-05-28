class Solution {
public:
    int maximumSwap(int num) {
        pair<int, int> toSwap = {-1, -1};
        vector<int> digits = splitNum(num);

        int highestId = digits.size() - 1;
        for (int i = digits.size() - 2; i >= 0; i -= 1) {
            if (digits[i] < digits[highestId]) {
                toSwap = {i, highestId};
            }
            if (digits[i] > digits[highestId]) {
                highestId = i;
            }
        }

        if (toSwap.first != -1) {
            swap(digits[toSwap.first], digits[toSwap.second]);
        }
        return mergeNum(digits);
    }

private:
    vector<int> splitNum(int num) {
        vector<int> ans;
        while (num > 0) {
            ans.push_back(num % 10);
            num /= 10;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }

    int mergeNum(const vector<int> &digits) {
        int num = 0;
        for (auto d : digits) {
            num = num * 10 + d;
        }
        return num;
    }
};