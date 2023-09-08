def solution(numbers):
    answer = 0
    
    no_num_dict = {i:0 for i in range(10)}
    
    for num in numbers:
        no_num_dict[num] += 1
        
    for key, value in no_num_dict.items():
        if value == 0:
            answer += key
    
    return answer


# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86051