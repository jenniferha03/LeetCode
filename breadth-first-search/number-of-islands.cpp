class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        for (int i = 0; i < grid.size(); i += 1) {
            for (int j = 0; j < grid[i].size(); j += 1) {
                if (grid[i][j] == '1') {
                    ans += 1;
                    dfs(grid, i, j);
                }
            }
        }

        return ans;
    }

private:
    vector<int> dx = {0, -1, 0, 1};
    vector<int> dy = {-1, 0, 1, 0};

    void dfs(vector<vector<char>> &grid, int i, int j) {
        grid[i][j] = '#';

        for (int k = 0; k < dx.size(); ++k) {
            int newX = i + dx[k];
            int newY = j + dy[k];

            if (newX < 0 || newY < 0 || newX >= grid.size() || newY >= grid[0].size()) continue;

            if (grid[newX][newY] != '1') continue;
            dfs(grid, newX, newY);
        }
    }
};