class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> m;

        for (auto c : s) {
            m[c] += 1;
        }

        bool hasOdd = false;
        for (auto e : m) {
            if (e.second % 2 == 1) {
                if (hasOdd) {
                    return false;
                }
                hasOdd = true;
            }
        }

        return true;
    }
};