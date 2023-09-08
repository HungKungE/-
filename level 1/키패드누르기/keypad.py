def solution(numbers, hand):
    answer = ''
    
    key_pad = [['1','4','7','*'],['2','5','8','0'],['3','6','9','#']]
    
    left_pos = [0,3]
    right_pos = [2,3]
    
    for number in numbers:
        number = str(number)
        
        # 무조건 왼쪽
        if number in key_pad[0]:
                index = key_pad[0].index(number)
                left_pos[0] = 0
                left_pos[1] = index
                answer += 'L'
        # 무조건 오른쪽       
        elif number in key_pad[2]:
                index = key_pad[2].index(number)
                right_pos[0] = 2
                right_pos[1] = index
                answer += 'R'
        # 더 가까운거       
        elif number in key_pad[1]:
                pos = [1, key_pad[1].index(number)]
                
                if get_distance(left_pos, pos) > get_distance(right_pos, pos) :
                    right_pos = pos
                    answer += 'R'
                elif get_distance(left_pos, pos) < get_distance(right_pos, pos) :
                    left_pos = pos
                    answer += 'L'
                elif get_distance(left_pos, pos) == get_distance(right_pos, pos) :
                    if hand == 'left':    
                        left_pos = pos
                        answer += 'L'
                    elif hand == 'right':    
                        right_pos = pos
                        answer += 'R'
    
    return answer

def get_distance(a, b):
    return abs(int(a[0])-int(b[0])) + abs(int(a[1])-int(b[1]))

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/67256