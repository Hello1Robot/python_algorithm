# 최종적으로 설정된 name을 토대로 메세지 출력하기
# 닉네임이 변경되는 경우는 2가지
# 나갔다가 새로운 닉네임으로 들어오기
# 안에서 Change로 변경하기
# 딕셔너리로 만들어서 값 넣어주면 될 듯?

def solution(record):
    answer = []
    user_dict = {}
    order_list = []
    for info in record:
        command, *userinfo = info.split()
        if len(userinfo) == 1:
            order_list.append((command, userinfo[0]))
            continue
        if command != 'Change':
            order_list.append((command, userinfo[0]))
        user_dict[userinfo[0]] = userinfo[1]
    
    for cmd, id in order_list:
        nick = user_dict[id]
        if cmd == 'Enter':
            answer.append(nick + '님이 들어왔습니다.' )
        else:
            answer.append(nick + '님이 나갔습니다.' )
        

    return answer



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))