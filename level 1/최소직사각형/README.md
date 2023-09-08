## 최소직사각형

1. 설명

모든 명함을 넣을 수 있는 최소 크기의 지갑 만드는 문제
</br>

2. 분석

</br>
간단하게 각 명함의 가로 세로 길이중에서 각각의 최대값에 해당하는 크기로 지갑을 만들면 되는 줄 알았는데
</br>
조금 더 조건을 생각해야하는 문제이다. 
</br>
어떤 명함은 눕히면 가로 세로 길이가 바뀌기 때문에 실제로 더 작은 지갑에 명함들을 다 넣을 수 있기 때문이다.
</br>
때문에 가로 세로 길이 배열을 sort하여 작은 길이는 가로, 큰 길이는 세로에 배치하여 해결했다.

3. 해결

</br>
```sh
    def solution(sizes):
    answer = 0
    
    max_size = [0, 0]
    
    for business_card in sizes:
        business_card.sort()
        
        if business_card[0] > max_size[0]:
            max_size[0] = business_card[0]
            
        if business_card[1] > max_size[1]:
            max_size[1] = business_card[1]
            
    answer = max_size[0] * max_size[1]
    
    return answer
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/86491)