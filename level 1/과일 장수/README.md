## 과일 장수 ( 쉽다 )

1. 설명
사과 상태 : 1 ~ k 점수
</br>
사과 상자 : 사과 m개
</br>
가격 : 사과 최하 품질이 p이면, 사과 상자는 p * m의 가격
</br>
상황 : 가능한 많은 사과를 팜 -> 얻을 수 있는 최대 이익 ( 남는 사과는 버림 + 상자 단위로만 팜 )
</br>
input : 사과 품질.list, 최대품질 k, 사과 상자의 사과 개수 m
</br>
output : 최대 이익
</br>

2. 분석

그리디알고리즘 문제 같다!
</br>
상자를 역순으로 정렬하고 m개씩 나눴다. ( 나머지는 버린다. )
</br>
그리고 순서대로 상자의 값을 계산했다.

3. 해결

</br>
```sh
def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    score_box_count = len(score) // m
    
    for i in range(score_box_count):
        answer = answer + min(score[i*m:(i+1)*m]) * m
        
    return answer
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/135808)