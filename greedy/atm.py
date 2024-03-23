# 제목: ATM
# 제공: 백준
# 번호: 11399
# URL: https://www.acmicpc.net/problem/11399
# 시간: 16시 43분 ~ 57분
# 결과: 성공
# 커멘트: 파이썬을 알아가는 과정...

n = input()
m = input()

sorted_time = sorted(list(map(int, m.split(" "))))

dp = [0]*int(n)

dp[0] = sorted_time[0]

for i in range(1, len(sorted_time)):
    dp[i] = dp[i-1] + sorted_time[i]
    
print(sum(dp))

# #사람의 수
# N = int(input())

# #인출에 걸리는 시간
# P = list(map(int, input().split()))

# #정렬
# P.sort()
# result = 0

# for i in range(1, len(P)+1):
#     result += sum(P[:i])

# print(result)