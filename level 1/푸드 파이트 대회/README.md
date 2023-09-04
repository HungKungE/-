## 푸드 파이트 대회 (쉬움)

1. 설명

음식 일렬로 배치
</br>
선수1(왼->오른) 선수2(오른->왼) 각 방향으로 이동하면서 순서대로 먹음
</br>
중앙에는 물 배치 -> 먼저 먹으면 이김
</br>
두 선수 음식의 종류, 양이 같아야함
</br>
칼로리는 외곽(낮음) -> 중앙(높음)
</br>
음식배치배열 반환
</br>
input:  칼로리가 적은 순서대로 음식의 양이 담겨 있음. food[0]은 항상 1 ( 물임 )
</br>

2. 분석

food[1:끝]까지 순서대로 확인
</br>
i번째 음식 개수 // 2 만큼 i를 문자열에 추가
</br>
순서대로 나열한 문자열 + 물("0") + 뒤집은 문자열을 반환

3. 해결

</br>
```sh
def solution(food):
    answer = ''
    
    half_answer = ''
    
    for i in range(1,len(food)):
        count = food[i]//2
        now_str = str(i) * count
        half_answer = half_answer + now_str
        
    answer = half_answer + str(0) + half_answer[::-1]
    
    return answer
```

- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/134240)