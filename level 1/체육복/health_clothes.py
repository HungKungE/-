def solution(n, lost, reserve):
    answer = 0
    # [2,0,0,2,2]
    student_cloth = {i:1 for i in range(1,n+1)}
    
    lost.sort()
    reserve.sort()
        
    for re in reserve:
        student_cloth[re] += 1
    
    for lo in lost:
        if student_cloth[lo] > 0:
            student_cloth[lo] -= 1
        
    for lo in lost:
        if lo == 1 and student_cloth[lo]==0:
            if student_cloth[lo+1] >= 2:
                #print("case1:","첫번째놈이 안가져옴 + 두번쨰 놈이 있음")
                student_cloth[lo] += 1
                student_cloth[lo+1] -= 1
        elif lo == n and student_cloth[lo]==0:
            if student_cloth[lo-1] >= 2:
                #print("case2:","n번째놈이 안가져옴 + n-1번쨰 놈이 있음")
                student_cloth[lo] += 1
                student_cloth[lo-1] -= 1
        elif lo >= 2 and lo <= n-1 and student_cloth[lo]==0:
            #print("case3:","중간놈이 안가져옴")
            if student_cloth[lo-1] >= 2:
                #print("case3-1:","중간놈 앞에놈이 가져옴")
                student_cloth[lo] += 1
                student_cloth[lo-1] -=1
            elif student_cloth[lo+1] >= 2:
                #print("case3-2:","중간놈 뒤에놈이 가져옴")
                student_cloth[lo] += 1
                student_cloth[lo+1]-=1
    
    count = 0
    
    for value in student_cloth.values():
        if value == 0:
            count +=1
    
    answer += n - count
    
    return answer

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/42862#