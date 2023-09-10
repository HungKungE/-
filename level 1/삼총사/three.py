def solution(number):
    answer = 0
    
    for i, num in enumerate(number):
        first = num
        for j in range(i+1,len(number)):
            second = number[j]
            for k in range(j+1,len(number)):
                third=number[k]
                #print("(",first, ",", second, ",",third,")")
                if first+second+third==0:
                    #print("Ok!")
                    answer=answer+1

    return answer