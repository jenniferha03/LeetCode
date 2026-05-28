class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        vector<vector<int>> result(mat.size(), vector<int>(mat[0].size(), INT_MAX));
        queue<pair<int, int>> q;

        for (int i = 0; i < mat.size(); ++i) {
            for (int j = 0; j < mat[0].size(); ++j) {
                if (mat[i][j] == 0) {
                    q.push({i, j});
                    result[i][j] = 0;
                }
            }
        }

        while (!q.empty()) {
            pair<int, int> cell = q.front();
            q.pop();

            for (int i = 0; i < dx.size(); ++i) {
                int x = cell.first + dx[i];
                int y = cell.second + dy[i];

                if (x < 0 || x >= mat.size() || y < 0 || y >= mat[0].size()) {
                    continue;
                } 

                if (result[x][y] > result[cell.first][cell.second] + 1) {
                    result[x][y] = result[cell.first][cell.second] + 1;
                    q.push({x, y});
                }
            }
        }
    
        return result;
    }

private:
    vector<int> dx = {0, -1, 0, 1};
    vector<int> dy = {-1, 0, 1, 0};
};