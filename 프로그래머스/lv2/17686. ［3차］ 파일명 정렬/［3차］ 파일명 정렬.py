def divide(x):
    head = ''
    number = ''
    tail = ''

    start = 0
    end = len(x)
    flag = True
    for i in range(len(x)):
        if x[i].isnumeric():
            if not start:
                flag = False
                start = i
        
        elif not flag:
            end = i
            break
    
    head = x[:start]
    number = x[start:end]
    tail = x[end:]
    return (head, number, tail)

def solution(files):
    answer = []
    temp = []
    for file in files:
        temp.append(divide(file))

    temp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for a,b,c in temp:
        answer.append(a+b+c)
    return answer