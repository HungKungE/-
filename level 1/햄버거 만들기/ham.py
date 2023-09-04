'''
def solution(ingredient):
    answer = 0
    
    indi_str = "".join(str(s) for s in ingredient)
    
    hambuger = "1231"
    
    while True:
        start = indi_str.find(hambuger)
        
        if start==-1:
            break
        else :
            end = start+4
            indi_str = indi_str[:start] + indi_str[end:]
            answer = answer+1
    
    return answer
'''

def solution(ingredient):
    answer = 0
    
    cur_indi = []
    
    hambuger = [1,2,3,1]
    
    for i in ingredient:
        cur_indi.append(i)
        
        if cur_indi[-4:] == hambuger:
            del cur_indi[-4:]
            answer=answer+1
    
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))