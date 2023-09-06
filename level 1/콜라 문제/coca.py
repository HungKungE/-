def solution(a, b, n):
    answer = 0
    
    give_coca = a
    receive_coca = b
    empty_coca = n

    while True :
        
        new_coca = (empty_coca // give_coca)
        
        if new_coca == 0 :
            break
            
        new_coca = new_coca * receive_coca
        answer = answer + new_coca
        
        empty_coca = (empty_coca % give_coca) + new_coca
        
    return answer