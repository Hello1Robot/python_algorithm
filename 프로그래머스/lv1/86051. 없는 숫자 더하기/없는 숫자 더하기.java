import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


class Solution {
	public int solution(int[] numbers) {
		Set<Integer> num_set = new HashSet<>(Arrays.asList(Arrays.stream(numbers).boxed().toArray(Integer[]::new)));
		int sum = 0;
		for (Integer integer : num_set) {
			sum += integer;
		}
		return 45-sum;
	}
}