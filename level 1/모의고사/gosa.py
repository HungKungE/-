def solution(answers):
    answer = []
    
    stu_one = [1,2,3,4,5]
    
    stu_two = [2,1,2,3,2,4,2,5]
    
    stu_three = [3,3,1,1,2,2,4,4,5,5]
    
    corrects=[0,0,0]
    
    # 채점
    for i, ans in enumerate(answers):
        one_index=i
        two_index=i
        three_index=i
        
        if one_index >=5:
            one_index = one_index % 5
        if two_index >=8:
            two_index = two_index % 8
        if three_index >=10:
            three_index = three_index % 10
        
        if stu_one[one_index]==ans:
            corrects[0]+=1
        if stu_two[two_index]==ans:
            corrects[1]+=1
        if stu_three[three_index]==ans:
            corrects[2]+=1
    
    # 많이 맞힌 사람
    # 똑같은 점수면 다 넣어
    max_correct = max(corrects)
    
    for i, correct in enumerate(corrects):
        if correct==max_correct:
            answer.append(i+1)
        
    return answer


print(solution([1,2,3,4,5]))