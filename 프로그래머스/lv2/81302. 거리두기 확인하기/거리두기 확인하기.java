import java.util.ArrayList;
import java.util.List;


public class Solution {

	private static class Point{
		public final int x, y, z;
		private Point(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}

	}


		private final int[] dx = {0,1,0,-1};
		private final int[] dy = {1,0,-1,0};

		private int check_distance(char[][] field, int size){

			List<Point> ps = new ArrayList<>(); // 정점 저장할 리스트 선언
			for (int i = 0; i < size; i++) {    // 탐색할 정점 집어넣기
				for (int j = 0; j < size; j++) {
					if(field[i][j] == 'P'){
						ps.add(new Point(i,j,-1));
					}
				}
			}
			int level = 0;
			while(!ps.isEmpty() && level < 2){
				List<Point> new_ps = new ArrayList<>();
				for (Point p : ps) {
					for (int i = 0; i < dx.length; i++) {
						if(p.z == i){
							continue;
						}
						int nx = p.x + dx[i];
						int ny = p.y + dy[i];
						if(nx < 0 || nx >= size || ny < 0 || ny >= size){
							continue;
						}
						if(field[nx][ny] == 'P'){
							return 0;
						}
						if(field[nx][ny] == 'O'){
							new_ps.add(new Point(nx,ny,(i+2)%4));
						}

					}
				}
				level++;
				ps = new_ps;
			}
			return 1;
		}

		public int[] solution(String[][] places) {
			int size = places.length;
			int[] answer = new int[size];
			for (int i = 0; i < size; i++) { // places 순회하면서 가능 여부 확인
				String[] place = places[i]; // 검사 할 대기실
				char[][] field = new char[size][];  // 대기실을 이차원배열화시키기(String을 하나씩 나눠야함)
				for (int j = 0; j < size; j++) {
					field[j] = place[j].toCharArray();
				}
				answer[i] = check_distance(field, size);
			}
			return answer;
		}

}