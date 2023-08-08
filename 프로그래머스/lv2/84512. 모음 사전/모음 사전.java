import java.util.ArrayList;
import java.util.List;

class Solution {
	private static final char[] CHARS = {'A','E','I','O','U'};

	private int generate(String word, String original, List<String> wordList) {
		wordList.add(word);

		if(word.equals(original)){
			return wordList.size()-1;
		}

		if (word.length() == 5) {
			return 0;
		}
		for (char aChar : CHARS) {
			int a = generate(word+aChar, original, wordList);
			if(a != 0){
				return a;
			}
		}
		return 0;
	}

	public int solution(String word){
		List<String> wordList = new ArrayList<>();
		return generate("", word, wordList);
	}
}