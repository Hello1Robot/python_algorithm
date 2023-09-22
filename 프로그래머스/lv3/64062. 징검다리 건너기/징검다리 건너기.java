class Solution {
	public int solution(int[] stones, int k) {

		int start = 1;
		int end = 200000000;

		while(start <= end){
			int mid = (start+end)/2;
			boolean flag = false;
			int consecutiveEmpty = 0;

			for (int i = 0; i < stones.length; i++) {
				int stone = stones[i] - mid;
				if (stone <= 0) {
					consecutiveEmpty++; // 연속으로 비어있는 돌 수 증가
					if (consecutiveEmpty >= k) {
						flag = true;
						break;
					}
				} else {
					consecutiveEmpty = 0; // 연속으로 비어있는 돌 수 초기화
				}
			}
			if(flag) end = mid-1;
			else start = mid+1;

		}


		return start;
	}
}