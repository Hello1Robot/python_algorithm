import sys
input = sys.stdin.readline
N = int(input())
nums = [float(input()) for _ in range(N)]
# 생각부터 적자
# 파이썬은 슬라이싱을 쓰면 될 듯
# pop과 append를 쓰는 건 어떨까
# 이중 리스트로 만들어 둠
# 원소 하나 꺼냄(팝) - 반으로 슬라이싱해서 나눠담음 - 리스트에 어펜드
# while len(nums[0]) > 1:
#     num = nums.pop(0)
#     if len(num) % 2:
#         num_a, num_b = num[0:len(num)//2+1], num[len(num)//2+1:]
#     else:
#         num_a, num_b = num[0:len(num)//2], num[len(num)//2:]        
#         nums.append(num_a)
#         nums.append(num_b)
# print(nums)
nums.sort()
for i in range(7):
    print(f'{nums[i]:.3f}')