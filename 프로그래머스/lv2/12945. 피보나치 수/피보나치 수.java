class Solution {
	private final int[] fibos = new int[1000000];

	public int solution(int n) {
		fibos[0] = 1;
		fibos[1] = 1;
		for (int i = 2 ; i <= n; i++) {
			fibos[i] = (fibos[i-2]+fibos[i-1])%1234567;
		}
		return fibos[n-1];
	}
}