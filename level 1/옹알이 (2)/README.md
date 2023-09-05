## 옹알이 (2)

1. 설명

애기가 옹알이를 하는데 발음을 4개밖에 못함
</br>
이 때, 특정 단어 문자열에서 애기가 발음할 수 있는 단어 수 구하는 문제임
</br>
애기는 같은 발음을 2번 이상 못함
</br>

2. 분석

처음에는 발음 가능한 모든 조합을 다 찾아서 대입해야하나 싶었는데
</br>
이전에 사용했던 스택 기법을 사용했더니 금방 풀렸다.
</br>
단어를 앞에서부터 슬라이싱해서 스택에 넣고
</br>
스택값이 발음 가능 배열에 있다면 처리하고, 없다면 지나간다.
</br>
처리했다면 last_delete에 넣어준다
</br>
그래서 만약 스택에서 한번 더 처리했는데 그 값이 last_delete에 있다면
</br>
연속된 발음이라서 해당 단어는 말할 수 없다.
</br>
그 외에도 스택에 값이 남는다면 발음 불가능한 단어이다.

3. 해결

```sh
    def solution(babbling):
        answer = 0

        # 발음 가능 단어들
        can_saying = ["aya", "ye", "woo", "ma"]
        

        for babble in babbling:
            # 마지막으로 제거한 발음
            last_delete = ""

            # 스택
            now_say = ""

            for bab in babble:
                now_say=now_say+bab
                
                if now_say in can_saying:
                    if now_say==last_delete:
                        break
                    else:
                        last_delete = now_say
                        now_say = ""
            # now_say가 초기화 되지 않았다면 발음 못하는 단어        
            if len(now_say)==0:
                answer=answer+1        
                    
        return answer
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/133499)