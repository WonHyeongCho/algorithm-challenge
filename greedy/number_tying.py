# 제목: 수 묶기
# 제공: 백준
# 번호: 1744
# 난이도: 골드 4
# URL: https://www.acmicpc.net/problem/1744
# 시간: 20시 00분 ~ 30
# 결과: 실패
# 커멘트: 하... 머리가 진짜 안돌아가는구만 더 열심히!!!

N = int(input())

plus = []
minus = []

result = 0

for i in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else: # 1은 무조건 더해준다.
        result += num
        
plus.sort(reverse=True)
minus.sort()

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i]*plus[i+1])
        
# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i]*minus[i+1])
        
print(result)