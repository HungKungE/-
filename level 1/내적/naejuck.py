def solution(a, b):
    answer = 0
    
    count = len(a)
    
    for i in range(count):
        answer += a[i]*b[i]
    
    return answer

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/70128