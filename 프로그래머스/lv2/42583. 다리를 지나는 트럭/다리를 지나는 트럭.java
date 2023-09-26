import java.util.ArrayDeque;
import java.util.Deque;


public class Solution {
	public int solution(int bridge_length, int weight, int[] truck_weights) {
		int answer = 0;
		Deque<Integer> que = new ArrayDeque<>();
		int total = 0;
		for (int i = 0; i < bridge_length; i++) {
			que.add(0);
		}
		int now = 0;
		while (now < truck_weights.length){
			total -= que.pollFirst();
			if(total+truck_weights[now] <= weight){
				que.add(truck_weights[now]);
				total+=truck_weights[now];
				now += 1;
			}
			else{
				que.add(0);
			}

			answer++;
		}

		while (total > 0){
			total -= que.pollFirst();
			answer++;
		}



		return answer;
	}
}