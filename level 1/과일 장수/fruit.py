def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    score_box_count = len(score) // m
    
    for i in range(score_box_count):
        answer = answer + min(score[i*m:(i+1)*m]) * m
        
    return answer


print(solution(3,4,	[1, 2, 3, 1, 2, 3, 1]))