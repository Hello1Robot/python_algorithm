class Solution {
	private int removeZero(String s){
		int zero = 0;
		for (char c : s.toCharArray()) {
			if(c == '0'){
				zero++;
			}
		}
		return zero;
	}

	public int[] solution(String s) {
		int[] answer = new int[2];
		int level = 0;
		int cnt = 0;
		while(!s.equals("1")){
			level++;
			int zero = removeZero(s);
			cnt += zero;
			int new_one = s.length() - zero;
			s = Integer.toString(new_one, 2);
		}

		answer[0] = level;
		answer[1] = cnt;
		return answer;
	}
}