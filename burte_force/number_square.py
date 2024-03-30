# 제목: 숫자 정사각형
# 제공: 백준
# 번호: 1051
# URL: https://www.acmicpc.net/problem/1051
# 시간: 11시 25분 ~ 50 분
# 결과: 성공
# 커멘트: 하.. 파이썬 문법 어렵다.

N, M = map(int, input().split())

square = [[int(i) for i in input()] for _ in range(N)]

max_length = min(N, M)

for length in range(max_length, 0, -1):
    real_length = length - 1
    for i in range(N-real_length):
        for j in range(M-real_length):
            if square[i][j] == square[i+real_length][j] == square[i][j+real_length] == square[i+real_length][j+real_length]:
                print(length**2)
                exit()

