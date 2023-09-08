def solution(n):
    answer = 0
    
    reverse_third = ''
    
    number = n
    
    while number > 0:
        reverse_third += str(number % 3)
        number = number // 3
    
    for index, num in enumerate(reverse_third):
        if num != '0':
            coefficient = len(reverse_third)-1-index
            answer += (3**coefficient)*int(num)
    
    
    return answer

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/68935