# 이진수로 만든 뒤
# 앞에 0을 추가한다. (1만 있는 경우를 방지 = 빈자리 만들기)
# 규칙 1. n보다 큰 자연수여야 한다.
# 규칙 2. 1의 갯수가 같아야 한다.
# 이기 때문에, 1을 오른쪽에서 왼쪽으로 이동시켜야 한다.
# 규칙 상 0은 올 수 없다.
# ======= 풀이 ========
# 가장 낮은 1을 찾는다.
# 해당 위치로부터 왼쪽으로 이동하며 0을 찾는다.
# 두 위치를 교환한다.

def solution(n):
    binary = list('0' + format(n, 'b'))
    start = -1
    end = -1
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            start = i
            break
    
    for j in range(start-1, -1, -1):
        if binary[j] == '0':
            binary[j] = '1'
            binary[start] = '0'
            end = j
            break
    
    etc = binary[end+1:]
    etc.sort()
    binary = binary[:end+1] + etc
    answer = int(''.join(b for b in binary),2)
    return answer