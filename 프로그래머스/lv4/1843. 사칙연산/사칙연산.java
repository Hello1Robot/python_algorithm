import java.util.Arrays;


public class Solution {

	private final int[][] max_mem = new int[202][202];
	private final int[][] min_mem = new int[202][202];

	private int max(int start, int end, String[] arr) {
		if (max_mem[start][end] != Integer.MIN_VALUE) { // 종료 조건
			return max_mem[start][end];
		}
		if (end - start == 1) return Integer.parseInt(arr[start]);

		int max = Integer.MIN_VALUE;
		for (int i = start + 1; i < end; i+=2) {
			int l = max(start, i, arr);
			int v;
			if (arr[i].equals("+")) {
				int r = max(i+1, end, arr);
				v = l + r;
			}
			else {
				int r = min(i+1, end, arr);
				v = l - r;
			}
			if (v > max) max = v;
		}
		return max_mem[start][end] = max;
		
	}

	private int min(int start, int end, String[] arr) {
		if (min_mem[start][end] != Integer.MAX_VALUE) {
			return min_mem[start][end];
		}
		if (end - start == 1) return Integer.parseInt(arr[start]); // 마지막에 오는 숫자일 경우

		int min = Integer.MAX_VALUE;
		for (int i = start+1; i < end; i+=2) {
			int l = min(start, i, arr);
			int v;
			if (arr[i].equals("+")) {
				int r = min(i+1, end, arr);
				v = l + r;
			}
			else {
				int r = max(i+1, end, arr);
				v = l - r;
			}
			if (v < min) min = v;
		}
		return min_mem[start][end] = min;

	}

	public int solution(String arr[]) {
		for (int[] row: max_mem){
			Arrays.fill(row, Integer.MIN_VALUE);
		}
		for (int[] row: min_mem){
			Arrays.fill(row, Integer.MAX_VALUE);
		}
		return max(0, arr.length, arr);
	}
}