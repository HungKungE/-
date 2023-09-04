'''
def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1):
        knight_power=getPower(i, limit, power)
        answer=answer+knight_power
    
    return answer

def getPower(number, limit, power):
    count = 0
    
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
    
    if count > limit:
        return power
    else :
        return count
'''




def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1):
        knight_power=getPower(i, limit, power)
        answer=answer+knight_power
    
    return answer

def getPower(number, limit, power):
    count = getDivisor(number)
    
    if count > limit:
        return power
    else :
        return count
    
def getDivisor(number):    
    divisor_count = 0
    
    for i in range(1,int(number**(1/2))+1):
        if number%i==0:
            if number//i == i:
                divisor_count=divisor_count+1
            else :
                divisor_count=divisor_count+2
                    
    print(divisor_count)
            
    return divisor_count
    
print("정답:",solution(5,3,2))