def if_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

N, M = map(int, input().split())

pocketmon_list = [input() for i in range(N)]

result_list = [input() for i in range(M)]

for i in result_list:
    if if_integer(i) == False:
        print((pocketmon_list.index(i))+1)
    else:
        i = int(i)
        print(pocketmon_list[i-1])