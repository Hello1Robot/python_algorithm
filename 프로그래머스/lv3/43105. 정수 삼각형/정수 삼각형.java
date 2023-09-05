import java.util.Arrays;


public class Solution  {

	private final int[][] visited = new int[501][501];

	private int dp(int x, int y, int[][] triangle){
		if (x == triangle.length) return 0;
		if (visited[x][y] != -1) return visited[x][y];

		return visited[x][y] = triangle[x][y] + Math.max(dp(x+1, y, triangle), dp(x+1, y+1, triangle));

	}

	public int solution(int[][] triangle) {
		for (int[] ints : visited) {
			Arrays.fill(ints, -1);
		}
		return dp(0,0,triangle);
	}
}
