import java.util.Arrays;
import java.util.Comparator;

class Solution {
	public String[] solution(String[] strings, int n) {
		Arrays.sort(strings, (s1, s2) -> {
			if (s1.charAt(n) != s2.charAt(n)){  // 문자가 다를때만
				return s1.charAt(n) - s2.charAt(n); // 해당 인덱스로 정렬
			}
			return s1.compareTo(s2); // 해당 인덱스의 문자가 같으면, 사전순 정렬
		});
		return strings;
	}
}