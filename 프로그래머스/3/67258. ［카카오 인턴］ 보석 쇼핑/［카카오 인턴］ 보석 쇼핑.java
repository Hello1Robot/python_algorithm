import java.util.HashMap;


public class Solution {
	public int[] solution(String[] gems) {
		HashMap<String, Integer> gemMap = new HashMap<>();
		// 약간 while 로 현재 gem이랑 같으면 여러 번 start 올리기
		int start = 0;
		int x = 0;
		int y = 0;
		for (int i = 0; i < gems.length; i++) {
			if(!gemMap.containsKey(gems[i])){
				gemMap.put(gems[i], 1);
				x = start;
				y = i;
				continue;
			}
			gemMap.put(gems[i], gemMap.get(gems[i])+1);
			while(gemMap.get(gems[start]) > 1 && start != i){
				gemMap.put(gems[start], gemMap.get(gems[start])-1);
				start++;
				if(i-start < y-x){

					x = start;
					y = i;
				}
			}

		}
		return new int[]{x+1,y+1};
	}
}