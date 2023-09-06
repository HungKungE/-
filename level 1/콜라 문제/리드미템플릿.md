## 콜라 문제 ( 쉬움 )

1. 설명

</br>
콜라 빈 병 2개를 가져다주면 콜라 1병을 주는 마트가 있다.
</br>
빈 병 20개를 가져다주면 몇 병을 받을 수 있는가?
</br>
단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
</br>
위 문제를 일반화 시키는 코드를 만드는 게 이번 문제이다.
</br>

2. 분석

</br>
빈 콜라 병을 a개 가져가면 새 콜라 b개로 바꿔준다고 하자.
</br>
이 때, 가지고 있는 빈 콜라 병은 n개라고 해서 문제를 풀었다.
</br>
</br>
바꾼 새 콜라는 다시 빈 병이 될 수 있기 때문에
</br>
현재 가지고 있는 빈 병 개수 // a 가 0이 될 때까지
</br>
총 얻을 수 있는 콜라 개수에 새로 얻는 콜라 개수를 추가한다.
</br>
그리고 남은 빈 콜라병에 새로 얻은 콜라 개수를 더한다. 

3. 해결

</br>
```sh
    def solution(a, b, n):
        answer = 0
        
        give_coca = a
        receive_coca = b
        empty_coca = n

        while True :
            
            new_coca = (empty_coca // give_coca)
            
            if new_coca == 0 :
                break
                
            new_coca = new_coca * receive_coca
            answer = answer + new_coca
            
            empty_coca = (empty_coca % give_coca) + new_coca
            
        return answer
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/132267)