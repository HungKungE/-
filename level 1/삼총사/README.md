## 삼총사

1. 설명

n명의 학생 중에, 3명의 학생번호를 더했을 때 0이 되는 set의 개수를 구하는 문제
</br>

2. 분석

3중 for문으로 해결함!
</br>
다른 사람들 풀이를 보니까 간결하길래 어떻게 했나 봤는데
</br>
from itertools import combinations를 사용하는 걸 봄
</br>
```sh   
    from itertools import combinations
    
    def solution (number) :
        cnt = 0
        for i in combinations(number,3) :
            if sum(i) == 0 :
                cnt += 1
        return cnt
```

3. 해결

</br>
```sh
    def solution(number):
        answer = 0
        
        for i, num in enumerate(number):
            first = num
            for j in range(i+1,len(number)):
                second = number[j]
                for k in range(j+1,len(number)):
                    third=number[k]
                    #print("(",first, ",", second, ",",third,")")
                    if first+second+third==0:
                        #print("Ok!")
                        answer=answer+1

        return answer
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/131705)