## 햄버거 만들기 ( 쉬움 )

1. 설명

햄버거 재료가 순서대로 정렬된 배열이 제공됨
</br>
그 재료들의 순서가 1,2,3,1 이면 햄버거가 됨
</br>
순서대로 만들 수 있는 햄버거 개수 찾기

2. 분석

햄버거를 만드는 최대 개수를 찾는 문제가 아니다.
</br>
순서대로 정렬된 재료 중에서 1,2,3,1인 재료를 없애고 햄버거 개수 + 1하고
</br>
다시 남은 재료 중에서 1,2,3,1인 재료를 없애는 식을 반복한다.
</br>
</br>
처음에는 재료 배열 -> 문자열로 바꿔 문제를 풀려고 했다
</br>
이 잘못된 생각 때문에 시간초과의 늪에 빠져 많은 시간을 낭비했다.
</br>

```sh
def solution(ingredient):
    answer = 0
    
    indi_str = "".join(str(s) for s in ingredient)
    
    hambuger = "1231"
    
    while True:
        
        count = indi_str.count(hambuger)
        #print(indi_str,"에는",hambuger,"가",count,"개 있음")
        if count == 0:
            break
        
        else :
            indi_str = indi_str.replace(hambuger,"",count)
            answer = answer + count
    
    return answer
```

</br>
이 문제는 스택을 사용하는 게 해결책이었다.


3. 해결

</br>
```sh
def solution(ingredient):
    answer = 0
    
    cur_indi = []
    
    hambuger = [1,2,3,1]
    
    for i in ingredient:
        cur_indi.append(i)
        
        # 이게 인덱스 에러가 인뜨는 이유 : 파이썬은 할 수 있는 데까지만 슬라이싱함
        if cur_indi[-4:] == hambuger:
            del cur_indi[-4:]
            answer=answer+1
    
    return answer
```


- [링크]()