# 제목: 잃어버린 괄호
# 제공: 백준
# 번호: 1541
# URL: https://www.acmicpc.net/problem/1541
# 시간: -
# 결과: 성공
# 커멘트: 첫 파이썬 풀이!

str = input()

def sumExpression(expression):
    numbers = expression.split("+")
    
    sum = 0
    
    for number in numbers:
        sum += int(number)
        
    return sum

answer = 0

expressions = str.split("-")

for i in range(0, len(expressions)):
    sum = sumExpression(expressions[i])
    if(i == 0) :
        answer += sum
    else:
        answer -= sum

print(answer)

# n = str(input())
# m = n.split('-')

# answer = 0
# # 첫번째는 -로 시작할 경우의 수가 있어서 따로 작업
# x = sum(map(int, (m[0].split('+'))))
# if n[0] == '-':
#     answer -= x
# else:
#     answer += x

# for x in m[1:]: # 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작
#     x = sum(map(int, (x.split('+'))))
#     answer -= x
# print(answer)