import java.util.HashSet;
import java.util.Set;


public class Solution {
	
	private boolean isPrime(int x){

		if (x <= 1) return false;

		for (int i = 2; i * i <= x; i++) {
			if (x % i == 0) return false;
		}

		return true;
	}

	private void getPrime(int num, int[] nums, boolean[] visited, Set<Integer> primes){
		if(isPrime(num)) primes.add(num);

		for (int i = 0; i < nums.length; i++) {
			if (visited[i]) continue;
			int nextNum = num * 10 + nums[i];

			visited[i] = true;
			getPrime(nextNum, nums, visited, primes);
			visited[i] = false;
		}

	}
	

	public int solution(String numbers) {
		Set<Integer> primes = new HashSet<>();
		int[] num_array = numbers.chars().map(c -> c - '0').toArray(); // 이 부분이 아직 좀 낯설다. map 관련은 자바나 자스나 비슷한데, 잘 안익혀지는듯
		getPrime(0, num_array, new boolean[num_array.length], primes);
		return primes.size();
	}
}