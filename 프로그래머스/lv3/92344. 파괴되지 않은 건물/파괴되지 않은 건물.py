# 제시되는 스킬은 type, x1, y1, x2, y2, degree 순
# type이 1일 때는 디그리만큼 낮추기
# type이 2일 때는 디그리만큼 높이기

# 확실히 지금 읽어보면, 결국 최종 상태만을 판별한다는 것을 알 수 있음
# 누적합을 어떻게 적용시키느냐가 관건이긴 함
# 그럼, 어디서 어디까지인지 보자
# 마진을 설정하는 게 나을까? -> 누적합을 적는 배열에만 마진을 설정해서 +1씩 하자
# 이외에는 큰 문제는 없을 듯
# 왼쪽에서 오른쪽으로 순회하며 누적합 적용시키는걸로 하자

def solution(board, skill):
    result = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    answer = 0
    for type, x1, y1, x2, y2, degree in skill:
        flag = -1
        if type == 2:
            flag *= -1
        
        result[x1][y1] += degree*flag
        result[x2+1][y2+1] += degree*flag
        result[x1][y2+1] -= degree*flag
        result[x2+1][y1] -= degree*flag
        
    for i in range(len(board)):
        for j in range(1,len(board[0])):
            result[i][j] += result[i][j-1]
    
    for i in range(len(board[0])):
        for j in range(len(board)):
            if j > 0:
                result[j][i] += result[j-1][i]
            if board[j][i] + result[j][i] > 0:
                answer+=1

        
    return answer