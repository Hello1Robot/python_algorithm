class Solution {
	public String solution(String new_id) {
		new_id = new_id.toLowerCase(); // 1단계 : 소문자로 치환
		new_id = new_id.replaceAll("[^a-z0-9\\-_.]",""); // 2단계 : 형식에 맞지 않는 문자열 제거
		new_id = new_id.replaceAll("\\.+","."); // 3단계 : 연속된 . 제거
		new_id = new_id.replaceAll("^\\.+|\\.+$", ""); // 4단계 : 처음이나 끝에 등장하는 마침표 제거. ^ = 문자열의 시작 / $ = 문자열의 끝
		if(new_id.isEmpty()) new_id = "a";  // 5단계 : 비어있으면 a
		if(new_id.length() > 15){       // 6단계 : 길이가 16자 이상이면 15개 문자 자르고, 끝에 마침표가 등장하면 없애기
			new_id = new_id.substring(0,15);
			new_id = new_id.replaceAll("\\.+$", "");
		}
		if(new_id.length()<3){  // 7단계 : 길이가 3 미만이면, 이상이 될 때까지 마지막 문자 반복
			while(new_id.length() < 3){
				new_id += new_id.charAt(new_id.length()-1);
			}
		}

		return new_id;
	}
}