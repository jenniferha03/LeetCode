class Solution {
public:
    int calculate(string s) {
        vector<long long> st;
        int id = 0;
        st.push_back(parseNumber(s, id));

        while (id < s.length()) {
            skipWhitespaces(s, id);
            if (id == s.length()) break;

            char op = s[id++];
            long long num = parseNumber(s, id);
            switch (op) {
                case '-':
                    st.push_back(-num);
                    break;
                case '+':
                    st.push_back(num);
                    break;
                case '*':
                    st.back() *= num;
                    break;
                case '/':
                    st.back() /= num;
                    break;
            }
        }

        int ans = 0;
        for (auto e : st) ans += e;
        return ans;
    }

private:
    long long parseNumber(const string &s, int &id) {
        long long num = 0;
        skipWhitespaces(s, id);
        while (id < s.length() && s[id] >= '0' && s[id] <= '9') {
            num = num * 10 + s[id] - '0';
            id += 1;
        } 
        return num;
    }

    void skipWhitespaces(const string &s, int &id) {
        while (id < s.length() && s[id] == ' ') id += 1;
    }
};