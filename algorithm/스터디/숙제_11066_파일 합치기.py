from queue import PriorityQueue
# 합치는 데 순서가 있을 것.
# 이거 DP가 맞나?
# 가장 큰 것과 작은 것을 넣으면 안되나?
# 아니 뭐지
# 30 30, 40 50 이렇게 해도 300인데? 흠
# 예시가 쉽지않음
# 그냥 작은 것끼리 합치는 거 맞지 않나
# 작은 거 두개 꺼내서 계산
# 합치고 계산하고 다시 넣기
# 프라이오리티큐를 만들고, qsize가 1일 때까지 반복
t = int(input())
for _ in range(t):
    N = int(input())
    nums = list(map(int,input().split()))
    que = PriorityQueue()
    tot = 0 # 비용 넣을 곳 생성
    # 큐에 값 집어넣기
    for num in nums:
        que.put(num)
    # 큐 사이즈가 1일 때 까지 하나씩 빼면서 비교하기.
    while que.qsize() > 1:
        a = que.get()
        b = que.get()
        c = a + b
        tot += c
        que.put(c)
    print(tot)

# Priority Queue를 쓰면서, 낮은 값끼리 합치면 될 거라고 생각했는데
# 문제에서 "이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고" 라는 조건을 충족시키지 못함
# 그래서 다시 생각해야되긴 할듯 ㅠ;
# 이건 파일합치기3의 답이었다... 프라이오리티 큐 대신 힙큐를 쓴
# 힙 큐 는 ! 멋젼