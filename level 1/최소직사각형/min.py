def solution(sizes):
    answer = 0
    
    max_size = [0, 0]
    
    for business_card in sizes:
        business_card.sort()
        
        if business_card[0] > max_size[0]:
            max_size[0] = business_card[0]
            
        if business_card[1] > max_size[1]:
            max_size[1] = business_card[1]
            
    answer = max_size[0] * max_size[1]
    
    return answer