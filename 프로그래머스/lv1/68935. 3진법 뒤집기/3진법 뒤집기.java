class Solution {
	public int solution(int n) {
		StringBuilder sb = new StringBuilder();
		sb.append(Integer.toString(n, 3));
		int answer = Integer.valueOf(sb.reverse().toString(), 3);
		return answer;
	}
}