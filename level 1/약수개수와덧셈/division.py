def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = get_division_count(i)
        
        #print(i,"의 약수갯수:",count)
        
        if count % 2 == 0:
            answer += i
        else :
            answer -= i
    
    return answer

def get_division_count(number):
    
    count = 0
    
    for num in range(1,int(number**(1/2))+1):
        if number % num == 0:
            #print(number,"의 약수:",num)
            if num == number**(1/2):
                #print("제곱근:",num)
                count += 1
            else:
                count += 2
    return count

print(solution(24,27))

# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77884