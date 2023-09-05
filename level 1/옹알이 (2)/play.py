def solution(babbling):
    answer = 0
    can_saying = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        last_delete = ""
        now_say = ""
        #print("시작:",babble)
        for bab in babble:
            now_say=now_say+bab
            #print(now_say)
            if now_say in can_saying:
                if now_say==last_delete:
                    break
                else:
                    last_delete = now_say
                    now_say = ""
        #print("끝:",babble)           
        if len(now_say)==0:
            #print("add")
            answer=answer+1        
                
    return answer


# print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))