# 제목: 미로 만들기
# 제공: 백준
# 번호: 2665
# URL: https://www.acmicpc.net/problem/2665
# 시간: 11시 11분 ~ 
# 결과: 실패...
# 커멘트: 생각보다 어렵다... 우선순위 Queue를 이용 or 다익스트라

import heapq

n = int(input())
maze = []
visited = [[False]*n for _ in range(n)]

for _ in range(n):
    line = input()
    maze.append(list(line))

# 동, 서, 북, 남
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y)) # 우선순위 큐
    
    while heap:
        count, cx, cy = heapq.heappop(heap)
        visited[cy][cx] = True # 방문 표시
        
        if cx == (n-1) and cy == (n-1):
            return count
        
        # 탐색
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if (0 <= nx < n) and (0 <= ny < n) and not visited[ny][nx]:
                visited[ny][nx] = True
                
                if maze[ny][nx] == 1:
                    heapq.heappush(heap, (count, nx, ny))
                else:
                    heapq.heappush(heap, (count+1, nx, ny))
                
print(bfs(0, 0))