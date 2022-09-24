# 애초에 보드 자체가 이차원리스트로 들어옴
# 세로축의 길이를 알 필요가 있음? 없나?
# 가공을 하는 게 나을까. 아닐까. 고민.
# 문제를 보면 사실 그냥 기능구현 자체는 쉽게 할 수 있음
# 타임을 어떻게 줄일까가 중요한 문제

def solution(board, skill):
    for type, x1, y1, x2, y2, degree in skill:
        if type == 1:
            degree *= -1
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                board[i][j] += degree

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))

# 전부 시간초과가 나는 좋은 코드...
# 시간복잡도가 N*M*K이라서 당연히 터질 줄 알았음...
# 구현난이도는 낮지만 어떻게 더 효율적인 코드를 짤 수 있을지를 고민하게 해주는 문제.
# 질문에 있는 해설을 보고 구간합을 써서 푸는 문제라는 걸 알았지만, 사실 해설을 보지 않았으면 영원히 모를 부분이긴 함
# 부분합을 이용하는 방법 하나만 얻어가도 이 문제를 풀려고 노력한 보람이 있을 것.
# https://school.programmers.co.kr/questions/25471
# 수요일에 누적합 이야기를 조금 하면 좋겠다 이거
# 약간 뭐라해야되지? 도원이같은 경우에는 자료구조를 달리 하면서 풀려고 노력했는데
# 조금 더 다른 수학적인 접근이라서 약간 진짜 새로운 거 배운 느낌?
# 풀이를 봤는데도 아쉽지 않아. 근데 솔직히 풀이를 보고도 헷갈리는 부분들이 있어서, 그 부분들을 조금 처리해야 될 것 같음.