class Solution {
	public int[] solution(long n){
		// charAt으로 접근하는 방법
		String s = Long.toString(n);
		int[] answer = new int[s.length()];
		for (int i = s.length()-1; i >= 0 ; i--) {
			answer[s.length()-i-1] = s.charAt(i) - '0';
		}
		

		return answer;
	}
}