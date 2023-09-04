## 기사단원의 무기 ( 어렵다 )

1. 설명

number명의 기사들은 1 ~ number 까지 번호가 지정되어 있다.
</br>
기사는 자신의 번호의 약수의 개수에 해당하는 공격력을 가진 무기를 구매한다.
</br>
이 때, 공격력이 limit을 넘으면 지정된 공격력(power)의 무기를 사야한다.
</br>
이 경우에 number명의 기사들이 사야 할 무기 공격력의 총 합을 구해야 한다.
</br>

2. 분석

이 문제의 핵심은 숫자의 약수의 개수를 구하는 로직이라고 생각한다.
</br>
아래는 단순하게 약수의 개수를 구하는 코드이다.
</br>

```sh
    count = 0
    
    # 1 ~ number까지 나눠서 나머지가 0아면 약수
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
```

</br>
위 코드는 직관적이지만 1부터 number까지 모든 수를 검사하기 때문에 number가 커질수록 소요시간이 커진다.
</br>
따라서 좀 더 효율적인 로직을 생각해 내야한다.
</br>
</br>

3. 해결
약수는 보통 짝을 이룬다.
</br>
15 의 약수는 1, 3, 5, 15이다.
</br>
(1, 15), (3, 5)가 짝을 이루기 때문에 1, 3을 검사했다면 굳이 5, 15를 검사할 필요가 없다.
</br>
때문에 약수들의 중간값만 알 수 있다면 시행횟수를 절반으로 줄일 수 있다.
</br>
number의 약수들의 중간값을 처음에는 단순하게 number/2하면 되는거 아님?
</br>
이라고 생각해서 구현했는데 아니었다.
</br>
당연하지. 15만 봐도 1, 3, 5, 15인데 15//2 는 7이니까!
</br>
</br>
힌트는 약수의 개수가 홀수인 수에서 찾을 수 있었다.
</br>
16은 약수가 1, 2 ,4, 8, 16이다.
</br>
4를 기준으로 나머지 약수들은 짝을 이루는 것을 알 수 있다.
</br>
따라서 약수들의 중간값은 해당 정수의 제곱근이라고 생각했다.
</br>
위 생각을 토대로 구현한 코드는 다음과 같다.
</br>
```sh
def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1):
        knight_power=getPower(i, limit, power)
        answer=answer+knight_power
    
    return answer

# 무기 공격력 결정하는 함수
def getPower(number, limit, power):
    count = getDivisor(number)
    
    if count > limit:
        return power
    else :
        return count

# 약수 개수 구하는 함수
def getDivisor(number):    
    divisor_count = 0
    
    for i in range(1,int(number**(1/2))+1):
        if number%i==0:
            if number//i == i:
                divisor_count=divisor_count+1
            else :
                divisor_count=divisor_count+2
            
    return divisor_count
```


- [링크](https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3)