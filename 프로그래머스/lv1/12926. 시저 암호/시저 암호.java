// 이거는 배열화시켜서 새로 담기?
// 책에서 char[]를 만드는 걸 좋아하던데
// 여기도 크게 다르지는 않을 듯

class Solution {
	public char push(char c, int n){
		if(c == ' ') return c;

		int offset = Character.isUpperCase(c) ? 'A' : 'a'; // 대문자면 A, 소문자면 a를 반환하는 삼항연산자
		int position = (c - offset + n) % 26;
		return (char) (offset + position);

	}

	public String solution(String s, int n) {
		StringBuilder sb = new StringBuilder();
		for (char c : s.toCharArray()) {
			sb.append(push(c, n));
		}
		return sb.toString();
	}
}