class Solution {
	public String solution(int n, int t, int m, int p) {
		StringBuilder sb = new StringBuilder();
		int num = 0;
		while (sb.length() < (m*t)){
			sb.append(Integer.toString(num++, n));
		}
		StringBuilder answer = new StringBuilder();
		for (int i = 0; i < t; i++) {
			answer.append(sb.charAt((p-1)+(m*i)));
		}

		return answer.toString().toUpperCase();
	}
}