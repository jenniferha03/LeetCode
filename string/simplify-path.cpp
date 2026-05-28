class Solution {
public:
    string simplifyPath(string path) {
        int id = 0;
        vector<string> st;

        while (id < path.length()) {
            string name = parseName(path, id);
            if (name == "" || name == ".") continue;
            if (name == "..") {
                if (st.size() > 0) st.pop_back();
            } else {
                st.push_back(name);
            }
        }

        string ans = "";
        for (auto e : st) {
            ans += "/" + e;
        }
        if (ans == "") ans += "/";
        return ans;
    }

private:
    string parseName(const string &path, int &id) {
        string name = "";
        skipSlashes(path, id);
        while (id < path.length() && path[id] != '/') {
            name.push_back(path[id++]);
        }
        return name;
    }

    void skipSlashes(const string &path, int &id) {
        while (id < path.length() && path[id] == '/') id += 1;
    }
};