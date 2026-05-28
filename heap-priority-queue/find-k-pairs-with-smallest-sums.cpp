class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        // Priority queue store {sum, nums1_index, nums2_index}
        priority_queue<vector<int>, vector<vector<int>>, Compare> pq;
        for (int i = 0; i < nums1.size(); ++i) {
            pq.push({nums1[i] + nums2[0], i, 0});
        }

        vector<vector<int>> ans;
        while (k > 0) {
            auto el = pq.top();
            pq.pop();

            ans.push_back({nums1[el[1]], nums2[el[2]]});

            if (el[2] + 1 < nums2.size()) {
                pq.push({nums1[el[1]] + nums2[el[2] + 1], el[1], el[2] + 1});
            }
            k -= 1;
        }

        return ans;
    }

private:
    struct Compare {
        bool operator()(vector<int> const & a, vector<int> const & b) {
            return a[0] > b[0];
        }
    };
};