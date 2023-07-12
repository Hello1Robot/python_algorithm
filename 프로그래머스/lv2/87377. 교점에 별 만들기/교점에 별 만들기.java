// 예시에서 별을 그리긴 했는데
// 별을 그리는 문제는 아니고
// 교점 중 정수인 좌표평면에 *을 찍는 거다.
// 그럼 answer가 String배열인데
// 이거 약간 배열을 String화 시키는 게 조금 귀찮을 거 같다 개인적으로는
// Java라서 어려운 부분?
// 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않는다 = 겹치는 건 없다는 뜻
// A와 B 둘 중 하나는 기울기가 있다 = 무조건 직선으로 주어진다.
// 하나 이상 그려지는 입력만 주어진다.
// 서로 평행인 경우를 필터링하는 게 낫지 않을까 싶음
// 어차피 분모가 0이면 곤란하니까 애초에 if문으로 걸러야 되겠다

// ~~ 문제 풀이 시작 ~~
// 배열의 크기 = 모든 별을 포함하는 최소한의 크기이다.
// 즉 일단 별의 좌표들을 다 구한다
// 그런 다음, 별들 중 최대 x 와 최대 y 를 찾는다
// 그런 후 x 와 y를 토대로 해서 좌표 평면을 만든다.
// 별을 찍는다.

// 생각해 볼 점 : 좌표 평면 만들면서 별 찍을 수 있을까?
// 아니면 어차피 저거 선언 자체는 메모리만 많이 드니까
// 그냥 평면 만들어놓고 해도 되나? 라는 생각

// 평소 프로그래밍 x,y가 아니라 수학의 x,y라서 좌표 헷갈리는듯

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


public class Solution {

	private static class Point {
		public final long x,y;

		private Point(long x, long y) {
			this.x = x;
			this.y = y;
		}

	}

	private Point crossPoint(long a1, long b1, long c1, long a2, long b2, long c2){
		if ((a1*b2)-(b1*a2) == 0){
			return null;
		}

		double x = (double) ((b1*c2)-(c1*b2)) / ((a1*b2)-(b1*a2));
		double y = (double) ((c1*a2)-(c2*a1)) / ((a1*b2)-(b1*a2));

		if (x%1 != 0 || y%1 != 0){
			return null;
		}

		return new Point((long)x,(long)y);

	}

	private Point getMinimumValue(Set<Point> points){
		long max_x = Long.MAX_VALUE;
		long max_y = Long.MAX_VALUE;
		for (Point point : points) {
			if(point.x < max_x){
				max_x = point.x;
			}
			if(point.y < max_y){
				max_y = point.y;
			}
		}

		return new Point(max_x,max_y);

	}

	private Point getMaximumValue(Set<Point> points){
		long min_x = Long.MIN_VALUE;
		long min_y = Long.MIN_VALUE;
		for (Point point : points) {
			if(point.x > min_x){
				min_x = point.x;
			}
			if(point.y > min_y){
				min_y = point.y;
			}
		}

		return new Point(min_x,min_y);

	}

	private int[] getSize(Point minValue, Point maxValue){

		int width = (int)(maxValue.x - minValue.x + 1);
		int height = (int)(maxValue.y - minValue.y + 1);

		return new int[] {width, height};
	}

	public String[] solution(int[][] line) {

		Set<Point> starPoints = new HashSet<>();
		for (int i = 0; i < line.length; i++) {
			for (int j = i+1; j < line.length; j++) {
				Point starPoint = crossPoint(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);

				if(null != starPoint){
					starPoints.add(starPoint);
				}
			}
		}
		Point maxValue = getMaximumValue(starPoints);
		Point minValue = getMinimumValue(starPoints);

		int[] size = getSize(minValue, maxValue);

		char[][] field = new char[size[1]][size[0]];
		for (char[] chars : field) {
			Arrays.fill(chars, '.');
		}

		for (Point starPoint : starPoints) {
			int x = (int) (starPoint.x - minValue.x);
			int y = (int) (maxValue.y - starPoint.y);
			field[y][x] = '*';
		}
		String[] answer = new String[field.length];
		for (int i = 0; i < answer.length; i++) {
			answer[i] = new String(field[i]);
		}

		return answer;
	}

}