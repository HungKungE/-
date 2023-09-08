    # lotto와 win_nums를 매칭
    # lotto의 0인 경우에는 자유 포인트 + 1
    # lotto의 번호가 win_nums안에 있으면 승리 포인트 + 1

def solution(lottos, win_nums):
    answer = []
    
    lottos.sort()
    win_nums.sort()
    
    win_point = 0
    free_point = 0
    
    for lotto in lottos:
        if lotto == 0:
            free_point+=1
        elif lotto in win_nums:
            win_point+=1
            
    max_point = 0
    min_point = 0
    
    if win_point + free_point < 2:
        max_point = 6
    else:
        max_point = 7 - (win_point + free_point)
        
    if win_point < 2:
        min_point = 6
    else:
        min_point = 7 - win_point
        
    answer.append(max_point)
    answer.append(min_point)
    
    return answer

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/77484