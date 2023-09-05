import java.util.HashMap;
import java.util.Map;

class Solution {
	public String solution(String[] participant, String[] completion) {
		Map<String, Integer> p_map = new HashMap<>();

		for (String sunsu : participant) {
			p_map.putIfAbsent(sunsu, 0);
			p_map.put(sunsu, p_map.get(sunsu)+1);
		}
		for (String wanju : completion) {
			p_map.put(wanju, p_map.get(wanju)-1);
		}

		for (String s : p_map.keySet()) {
			if(p_map.get(s) != 0){
				return s;
			}
		}

		return null;
	}
}