import java.util.ArrayList;
import java.util.List;

class Solution {
	public static int getSize(List<String> lst){
		StringBuilder sb = new StringBuilder();
		for (String s : lst) {
			sb.append(s);
		}
		return sb.toString().length();
	}

	public static int solution(String s) {
		int answer = s.length();


		for (int i = 1; i <= s.length()/2; i++) {
			int cnt = 1;
			List<String> repeat = new ArrayList<>();
			repeat.add("ㄱ");    // 임의의 문자 하나 넣어두기
			for (int j = 0; j < s.length(); j+=i) { // 이러면, 자르는 범위가 설정이 됨
				int endIndex = Math.min(j+i, s.length());
				String st = s.substring(j, endIndex);
				if(st.equals(repeat.get(repeat.size()-1))){
					cnt++;
				}
				else{
					if(cnt > 1){
						repeat.add(String.valueOf(cnt));
						cnt = 1;
					}
					repeat.add(st);
				}
			}
			if(cnt > 1){
				repeat.add(String.valueOf(cnt));
			}
			answer = Math.min(answer, getSize(repeat)-1);

		}

		return answer;
	}
}