class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1) return -1;
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid.size(), false));
        visited[0][0] = true;

        // <row, col, distance>
        queue<vector<int>> q;
        q.push({0, 0, 1});
        while (!q.empty()) {
            vector<int> e = q.front();
            q.pop();

            if (e[0] == n - 1 && e[1] == e[0]) {
                return e[2];
            }

            for (int i = 0; i < dx.size(); ++i) {
                int newX = e[0] + dx[i];
                int newY = e[1] + dy[i];
                if (newX < 0 || newY < 0 || newX >= n || newY >= n || grid[newX][newY] == 1 || visited[newX][newY]) continue;
                q.push({newX, newY, e[2] + 1});
                visited[newX][newY] = true;
            }
        }

        return -1;
    }

private:
    vector<int> dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    vector<int> dy = {0, -1, -1, -1, 0, 1, 1, 1};
};