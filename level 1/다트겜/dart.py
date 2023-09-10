def solution(dartResult):    
    point = []
    
    num=[str(i) for i in range(11)]
    bonus=["S","D","T"]
    prize=["*","#"]
    
    cur_point=''
    
    for result in dartResult:
        if result in num:
            cur_point+=result
            continue
        
        elif result in prize:
            if result=="*":
                if len(point)>=2:
                    point[-2]=point[-2]*2
                point[-1]=point[-1]*2
            elif result=="#":
                point[-1]=point[-1]*(-1)
        
        elif result in bonus:
            if cur_point==0:
                continue
                
            p = int(cur_point)
            
            if result=="S":
                p=p**1
            elif result=="D":
                p=p**2
            elif result=="T":
                p=p**3

            point.append(p)
            cur_point=''
    
    return sum(point)

print(solution("1S2D*3T"))