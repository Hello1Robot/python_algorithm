import java.util.*;

class Solution {
	private void count(int index, Set<String> banned, String[][] bans, Set<Set<String>> banSet){

		if (index == bans.length) {
			banSet.add(new HashSet<>(banned));
			return;
		}
		for (String id : bans[index]) {
			if (banned.contains(id)) continue;
			banned.add(id);
			count(index + 1, banned, bans, banSet);
			banned.remove(id);
		}
	}

	public int solution(String[] user_id, String[] banned_id) {
		String[][] bans = Arrays.stream(banned_id)
		                        .map(banned -> banned.replace('*', '.')) // 순회하면서 *을 다른 모든 문자를 뜻하는 정규표현식 . 으로 변경
		                        .map(banned -> Arrays.stream(user_id) // 변경한 것을 가지고 새로운 stream 진행
		                                             .filter(id -> id.matches(banned)) // 이번엔 user_id를 순회하며 매치되는 걸 filter
		                                             .toArray(String[]::new))
		                        .toArray(String[][]::new); // banned_id 와 user_id로 2차원 배열 만들기
		Set<Set<String>> banSet = new HashSet<>();
		count(0, new HashSet<>(), bans, banSet);
		return banSet.size();
	}
}