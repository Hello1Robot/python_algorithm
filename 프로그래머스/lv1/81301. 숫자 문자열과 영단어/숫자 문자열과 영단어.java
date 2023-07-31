class Solution {
	public int solution(String s) {
		String a = s.replace("zero", "0");
		String b = a.replace("one", "1");
		String c = b.replace("two", "2");
		String d = c.replace("three", "3");
		String e = d.replace("four", "4");
		String f = e.replace("five", "5");
		String g = f.replace("six", "6");
		String h = g.replace("seven", "7");
		String i = h.replace("eight", "8");
		String j = i.replace("nine", "9");
		return Integer.parseInt(j);
	}
}