import java.util.ArrayList;
import java.util.List;

class Solution {
	private void hanoi(int n, int from, int to, List<int[]> hanoiList){
		if (n == 1) {
			hanoiList.add(new int[] {from, to});
			return;
		}

		int empty = 6 - from - to;

		hanoi(n-1, from, empty, hanoiList);
		hanoi(1, from, to, hanoiList);
		hanoi(n-1, empty, to, hanoiList);

	}

	public int[][] solution(int n) {
		List<int[]> hanoiList = new ArrayList<>();
		hanoi(n, 1, 3, hanoiList);
		return hanoiList.toArray(new int[0][]);
	}
}