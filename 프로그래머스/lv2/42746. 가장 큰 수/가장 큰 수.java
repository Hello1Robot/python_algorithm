import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
	public String solution(int[] numbers) {
		return Arrays.stream(numbers)
			.mapToObj(String::valueOf) // mapToObj로 다른 형태로 변환 -> ValueOf로 String화 시킴
			.sorted((s1, s2) -> {
				int a1 = Integer.parseInt(s1+s2); // 하나만 더하는거라 String을 그냥 더하는 느낌인데 속도 상 문제없을까 싶음
				int a2 = Integer.parseInt(s2+s1);
				return a2-a1;
			})
			.collect((Collectors.joining(""))) // 파이썬의 join느낌으로 합치기
			.replaceAll("^0+", "0"); // 정규표현식으로 0일 경우 방지하기. 예외처리해도 될 듯.
	}
}