import random

def get_lotto():
    random_num = list(i for i in range(1,46))

    lotto = []

    while len(lotto) < 6 :
        cur_index = random.randrange(1,len(random_num))
        lotto.append(random_num[cur_index])
        del random_num[cur_index]
        
    lotto.sort()
    
    return lotto


for i in range(5):
    print(get_lotto())