import java.util.HashMap;
import java.util.Map;


public class Solution {
	
	private Map<Character, Integer> createMap(String word){
		Map<Character, Integer> map = new HashMap<>();
		for (char c : word.toCharArray()) {
			map.putIfAbsent(c, 0); // 존재하지 않으면 넣는 메서드. 알아두기
			map.put(c, map.get(c)+1);
		}

		return map;
	}
	
	public int solution(String before, String after) {
		return createMap(before).equals(createMap(after)) ? 1 : 0;
	}
}