# 32ms 14.2MB
class Solution:
    visited = [[1] * 101 if __ == 1 else [1 if _ == 1 else 0 for _ in range(101)] for __ in range(101)]
    def uniquePaths(self, m: int, n: int) -> int:
        if not self.visited[m][n]: # == False
            self.visited[m][n] = self.visited[n][m] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.visited[m][n]

# 28ms 14.1MB
class Solution2:
    visited = [[0 for _ in range(101)] for __ in range(101)]
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            self.visited[m][n] = self.visited[n][m] = 1
        elif not self.visited[m][n]: # == False
            self.visited[m][n] = self.visited[n][m] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.visited[m][n]

if __name__ == '__main__':
    s = Solution()
    a = s.uniquePaths(3,7)
    print(a)
