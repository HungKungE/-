## 성격유형검사
1. 설명

</br>
MBTI 같은 성격유형검사지를 통해서 사용자의 성격을 유추하는 로직을 만드는 문제
</br>

2. 분석

</br>
거의 하드 코딩으로 만들었다.
</br>
각 성격 별 점수 딕셔너리를 만들어서 해결했다.
</br>

3. 해결

</br>
```sh
    def solution(survey, choices):
        answer = ''
        
        survey_result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

        point_center = 4 #(1~7의 중간값은 4)
        
        for index, sur in enumerate(survey):
            point = choices[index]
            
            if point - point_center < 0:
                survey_result[sur[0]] += point_center - point
            elif point - point_center > 0:
                survey_result[sur[1]] += point - point_center
                
        if survey_result['R'] >= survey_result['T']:
            answer += 'R'
        else :
            answer += 'T'   
        
        if survey_result['C'] >= survey_result['F']:
            answer += 'C'
        else :
            answer += 'F'
            
        if survey_result['J'] >= survey_result['M']:
            answer += 'J'
        else :
            answer += 'M'
                
        if survey_result['A'] >= survey_result['N']:
            answer += 'A'
        else :
            answer += 'N'
        

        return answer
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/118666)