def solution(s):
    answer = ""
    
    num_str = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    num_dict = {num_str[i]:i for i in range(10)}
    
    word = ""
    
    for num_char in s:       
        if num_char >= 'a' and num_char <= 'z':
            word += num_char
            
            if word in num_str:
                answer += str(num_dict[word])
                word = ""
        else :
            answer += num_char
    
    return int(answer)

print(solution("one4seveneight"))