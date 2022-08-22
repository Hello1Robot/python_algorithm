import sys
input = sys.stdin.readline
# 회문이면 0, 유사회문이면 1, 둘 다 아니면 2를 출력
# 한 문자를 '삭제하면' 회문이 되는 것 = 유사회문
# 회문 검사방법은 아니까 유사회문을 생각해보자.
                # 짝수일 때 : 다 짝수인데 '단 두개만' 홀수일경우 - 유사회문
                # 그 이외의 경우에는 다 2.
                # 홀수일 때 : 여기는, 홀수인 게 3개다 = 2. 유사회문일 수 없음
                # 즉 홀수일 때는, 유사회문일 경우가 없다. 로 보면 될듯
# 아 위에건 다른 문제 접근법... 이건 반 잘라서 비교해봐야되는 친구네
# 짝수개 : 반 잘라서 앞뒤 비교. 같으면 0
# 만약 다를 경우, 앞뒤에 다른 카운트를 셈. 카운트가 1이면 1, 1을 넘기면 break하고 2 출력

# 홀수개 : 위랑 똑같은데.
# 그냥 가운데 거 삭제하고 위와 똑같이 비교해도 될 듯? = X
# xabba 이게 반례인데 이걸 어떻게 해결할 지 생각해야 됨.
# for 문 돌리면서 하나씩 빼고 회문검사 실시.
# 되는 게 있으면 유사회문


N = int(input())
for case in range(N):
    st = list(input())
    if len(st) % 2:
        res = 2
        cn = len(st) // 2
        for i in range(len(st)):
            new_st = st[:]
            new_st.pop(i)
            center = len(new_st)//2
            st_f = new_st[0:center]
            st_l = new_st[center:]
            st_l = st_l[::-1]
            if st_f == st_l:
                if i == cn:
                    res = 0
                else:
                    res = 1
        print(res)

    else:
        center = len(st)//2
        st_f = st[0:center]
        st_l = st[center:]
        st_l = st_l[::-1]
        uneq_cnt = 0
        for i in range(len(st_f)):
            if st_f[i] != st_l[i]:
                if i == center:
                    uneq_cnt = 1
                else:
                    uneq_cnt = 2
        print(uneq_cnt)
