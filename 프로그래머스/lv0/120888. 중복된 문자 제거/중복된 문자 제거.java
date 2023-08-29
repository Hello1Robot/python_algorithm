import java.util.HashSet;
import java.util.Set;

class Solution {
	public String solution(String my_string) {
		StringBuilder stb = new StringBuilder();
		Set<Character> characterSet = new HashSet<>();
		for (char c : my_string.toCharArray()) {
			if(characterSet.contains(c)) continue;

			characterSet.add(c);
			stb.append(c);

		}
		return stb.toString();
	}
}