'''
def solution(X, Y):
    answer = ''
    twine = []
    zero_count = 0
    
    for x in X:
        if x in Y:
            Y = Y.replace(x,"",1)
            twine.append(x)
            if x=="0":
                zero_count = zero_count + 1
    
    if zero_count == len(twine) and zero_count!=0:
        answer = "0"
    
    else :
        twine.sort(reverse=True)
        
        for i in twine:
            answer = answer + i
                
        if answer == '':
            answer="-1"
    
    return answer
'''

def solution(X, Y):
    answer = ''
    twine = []
    zero_count = 0
    
    x_count = [X.count(str(i)) for i in range(10)]
    y_count = [Y.count(str(i)) for i in range(10)]
    
    for i in range(10):
        if x_count[i]==0 or y_count[i]==0:
            continue
            
        duo = [x_count[i],y_count[i]]
        
        for j in range(min(duo)):
            if i == 0:
                zero_count = zero_count + 1
            twine.append(str(i))
    
    if zero_count == len(twine) and zero_count!=0:
        answer = "0"
    
    else :
        twine.sort(reverse=True)
        
        for i in twine:
            answer = answer + i
                
        if answer == '':
            answer="-1"
    
    return answer

#print("값",solution("100","2345"))