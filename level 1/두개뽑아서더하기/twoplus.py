from itertools import combinations

def solution(numbers):
    answer = []
    
            
    for i in combinations(numbers,2) :
        answer.append(sum(i))
    
    answer = list(set(answer))
    
    answer.sort()
    
    return answer

# 삼총사 문제에서 알게 된 combination을 사용했다.
# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 근데 sort와 list(set)의 순서를 바꾸면 몇개의 case가 실패하는 이유를 모르겠다.