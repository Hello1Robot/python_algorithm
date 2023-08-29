class Solution {
	private boolean isValid(long mid, int n, int[] times){
		long cnt = 0;
		for (int time : times) {
			cnt += mid / time;
		}
		return cnt >= n;
	}

	public long solution(int n, int[] times) {
		long start = 1;
		long end = 1000000000000000000L;

		while (end > start) {
			long mid = (start + end) / 2;
			if (isValid(mid, n, times)) end = mid; // n보다 클 경우, max 값 줄이기
			else start = mid + 1;  // n보다 작을 경우, min 값 줄이기
		}

		return start;
	}
}