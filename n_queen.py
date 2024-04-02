# 제목: N-Queen
# 제공: 백준
# 번호: 9663
# URL: https://www.acmicpc.net/problem/9663
# 시간: 11시 50분 
# 결과: 성공
# 커멘트: 하.. 파이썬 문법 어렵다.

N = int(input())
answer = 0

rows = [0]*N

def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == abs(x - i):
            return False
        
    return True

def n_queen(x):
    global answer
    if x == N:
        answer += 1
        return
    
    for i in range(N):
        rows[x] = i
        if check(x):
            n_queen(x+1)
            
n_queen(0)
print(answer)