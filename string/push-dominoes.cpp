class Solution {
public:
    string pushDominoes(string dominoes) {
        vector<int> closestLeft(dominoes.size(), INT_MAX);

        for (int i = dominoes.size() - 1; i >= 0; --i) {
            if (dominoes[i] == 'L') {
                closestLeft[i] = 0;
            } else if (dominoes[i] == 'R') {
                closestLeft[i] = INT_MAX;
            } else if (i != dominoes.size() - 1 && closestLeft[i+1] != INT_MAX) {
                closestLeft[i] = closestLeft[i+1] + 1;
            }
        }

        int closestRight = INT_MAX;
        for (int i = 0; i < dominoes.size(); ++i) {
            if (dominoes[i] == '.') {
                if (closestRight < closestLeft[i]) {
                    dominoes[i] = 'R';
                } else if (closestRight > closestLeft[i]) {
                    dominoes[i] = 'L';
                }
            } else if (dominoes[i] == 'R') {
                closestRight = 0;
            } else if (dominoes[i] == 'L') {
                closestRight = INT_MAX;
            }
            if (closestRight != INT_MAX) {
                closestRight += 1;
            }
        }

        return dominoes;
    }
};