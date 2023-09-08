def solution(price, money, count):
    answer = 0
    
    pay_money = 0
    
    for i in range(1, count+1):
        pay_money += price * i
    
    if money < pay_money:
        answer = pay_money - money
    
    return answer

# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/82612