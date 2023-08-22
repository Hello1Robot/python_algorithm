class Solution {
	public String solution(String s) {

		return s.chars() // chars -> IntStream으로 반환됨
		        .boxed()// Integer로 변환
		        .sorted((v1, v2) -> v2 - v1) // 내림차순 정렬
				.collect(StringBuilder::new,
					StringBuilder::appendCodePoint,
					StringBuilder::append)
				.toString();
	}
}