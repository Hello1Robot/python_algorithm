class Solution {
	private double getSlope(int x1, int y1, int x2, int y2){
		return (double) (y2-y1) / (x2-x1);
	}

	public int solution(int[][] dots) {

		for (int i = 1; i <= 2; i++) {
			if(getSlope(dots[0][0], dots[0][1], dots[i][0], dots[i][1]) == getSlope(dots[3-i][0], dots[3-i][1], dots[3][0], dots[3][1]))
				return 1;
		}

		return 0;
	}
}