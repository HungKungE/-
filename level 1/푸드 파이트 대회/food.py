def solution(food):
    answer = ''
    
    half_answer = ''
    
    for i in range(1,len(food)):
        count = food[i]//2
        now_str = str(i) * count
        half_answer = half_answer + now_str
        
    answer = half_answer + str(0) + half_answer[::-1]
    
    return answer