## 숫자 짝꿍

1. 설명

</br>
두 정수가 공통으로 가지고 있는 정수로 만들수 있는 가장 큰 정수 구하기
</br>
짝 없으면 -1
</br>
짝이 0만 있으면 0
</br>

2. 분석

</br>
처음에는 X의 원소를 하나씩 Y에 비교해서 문자열을 조정하면 될 줄 알았다.
</br>
이 생각을 가지고 만든 코드는 다음과 같다.
</br>

```sh
    def solution(X, Y):
        answer = ''
        twine = []
        zero_count = 0
        
        for x in X:
            if x in Y:
                Y = Y.replace(x,"",1)
                twine.append(x)
                if x=="0":
                    zero_count = zero_count + 1
        
        if zero_count == len(twine) and zero_count!=0:
            answer = "0"
        
        else :
            twine.sort(reverse=True)
            
            for i in twine:
                answer = answer + i
                    
            if answer == '':
                answer="-1"
        
        return answer
```
</br>
그런데 일부 테스트에서 시간 초과가 발생했다.
</br>
때문에 문자열을 직접 건드리는 방법에서
</br>
x, y에 있는 숫자의 수를 저장하는 배열을 만들고
</br>
각 index별로 비교하여 처리하도록 새로 코드를 짜서 해결했다.

3. 해결

</br>
```sh
def solution(X, Y):
    answer = ''
    twine = []
    zero_count = 0
    
    x_count = [X.count(str(i)) for i in range(10)]
    y_count = [Y.count(str(i)) for i in range(10)]
    
    for i in range(10):
        if x_count[i]==0 or y_count[i]==0:
            continue
            
        duo = [x_count[i],y_count[i]]
        
        for j in range(min(duo)):
            if i == 0:
                zero_count = zero_count + 1
            twine.append(str(i))
    
    if zero_count == len(twine) and zero_count!=0:
        answer = "0"
    
    else :
        twine.sort(reverse=True)
        
        for i in twine:
            answer = answer + i
                
        if answer == '':
            answer="-1"
    
    return answer
```


- [링크]()