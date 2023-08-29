import java.util.Arrays;

class Solution {
	private boolean isValid(int mid, int[] rocks, int n){
		int removed = 0;
		int last = 0;
		for (int rock : rocks) {
			if (rock - last < mid) {
				removed++;
				continue;
			}

			last = rock;
		}
		return removed <= n;
	}

	public int solution(int distance, int[] rocks, int n) {

		rocks = Arrays.copyOf(rocks, rocks.length+1);
		rocks[rocks.length-1] = distance; // 마지막 칸에 distance 추가
		Arrays.sort(rocks);

		int start = 1;
		int end = distance + 1;

		while (start + 1 < end) {
			int mid = (start + end) / 2;
			if (isValid(mid, rocks, n)) start = mid;
			else end = mid;


		}


		return start;
	}
}