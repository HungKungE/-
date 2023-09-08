def solution(survey, choices):
    answer = ''
    
    survey_result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for index, sur in enumerate(survey):
        point = choices[index]
        
        '''
        if point == 1 :
            survey_result[sur[0]] += 3
        elif point == 2 :
            survey_result[sur[0]] += 2
        elif point == 3 :
            survey_result[sur[0]] += 1
        elif point == 4 :
            continue       
        elif point == 5 :
            survey_result[sur[1]] += 1                
        elif point == 6 :
            survey_result[sur[1]] += 2        
        elif point == 7 :
            survey_result[sur[1]] += 3
        '''
        
        if point - 4 < 0:
            survey_result[sur[0]] += 4 - point
        elif point - 4 > 0:
            survey_result[sur[1]] += point - 4
            
    if survey_result['R'] >= survey_result['T']:
        answer += 'R'
    else :
        answer += 'T'   
    
    if survey_result['C'] >= survey_result['F']:
        answer += 'C'
    else :
        answer += 'F'
        
    if survey_result['J'] >= survey_result['M']:
        answer += 'J'
    else :
        answer += 'M'
            
    if survey_result['A'] >= survey_result['N']:
        answer += 'A'
    else :
        answer += 'N'
    

    return answer