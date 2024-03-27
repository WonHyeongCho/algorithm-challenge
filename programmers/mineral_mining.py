# 제목: 광물 캐기
# 제공: 프로그래머스
# 번호: 172927
# 난이도: level 2
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 시간: 20시 45분 
# 결과: 실패
# 커멘트: 예외 케이스를 못찾겠다...

picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]
values = {"diamond": 25, "iron": 5, "stone": 1}

answer = 0

dia_pick, iron_pick, stone_pick = picks

# 각 광물 이름을 해당하는 값으로 변환
converted_array = [values[mineral] for mineral in minerals]

print(converted_array)

new_array = []

for i in range(0, len(minerals), 5):
    index = int(i/5)
    if(i+5 > len(minerals)):
        new_array.append([index, sum(converted_array[i:])])
    else:
        new_array.append([index, sum(converted_array[i:i+5])])
        
new_array.sort(key= lambda x:x[1], reverse=True)

print(new_array)

for i in range(len(new_array)):
    if(dia_pick > 0):
        answer += 5
        dia_pick = dia_pick-1
    elif(iron_pick > 0):
        answer += int(new_array[i][1]/5) + int(new_array[i][1]%5)
        iron_pick = iron_pick-1
    elif(stone_pick > 0):
        answer += new_array[i][1]
        stone_pick = stone_pick-1
    else:
        break
    
print(answer)
