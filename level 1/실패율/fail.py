def solution(N, stages):
    answer = []

    dodals = [0 for _ in range(N+1)]
    fail = [0.0 for _ in range(N)]
    
    for stage in stages:
        dodals[stage-1]+=1
            
    for i, dodal in enumerate(dodals):
        if i == N:
            break
        
        '''
        pass_count = 0
        
        for j in range(i, len(dodals)):
            pass_count += dodals[j]
        '''
        
        pass_count = sum(dodals[i:])
        
        if pass_count == 0:
            fail[i] = 0
        else :        
            fail[i]= dodal / pass_count
        
    for _ in range(len(fail)):
        max_fail = max(fail)
        i = fail.index(max_fail)
        answer.append(i+1)
        fail[i]=-1
            
    return answer

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/42889