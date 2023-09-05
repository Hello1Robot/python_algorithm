public class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int MOD = 1000000007;
        int[][] dp = new int[m + 1][n + 1];
        boolean[][] isPuddle = new boolean[m + 1][n + 1];

        for (int[] puddle : puddles) {
            isPuddle[puddle[0]][puddle[1]] = true;
        }

        dp[1][1] = 1; // 출발 지점은 1로 초기화

        for (int x = 1; x <= m; x++) {
            for (int y = 1; y <= n; y++) {
                if (x == 1 && y == 1) continue; // 출발 지점은 이미 초기화했으므로 건너뜀
                if (isPuddle[x][y]) {
                    dp[x][y] = 0; // 물 웅덩이가 있는 경우 경로 없음
                } else {
                    dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % MOD; // 이전 경로 합산
                }
            }
        }

        return dp[m][n];
    }
}