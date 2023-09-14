def solution(r1, r2):
    cir_one=get_point_count(r1,1)
    cir_two=get_point_count(r2,2)
    #print(cir_one, cir_two)
    return cir_two - cir_one

def get_point_count(r,num):    
    y=r

    if num==1:
        # x축, y축 위의 점 추가 (작은 원 위의 점 제외)
        point = (r-1)*4 + 1
        for x in range(1, r):
            # 1사분면 위의 점 개수 * 4 (원 위의 점 제외)
            while x**2 + y**2 >= r**2:
                y=y-1
            point+= y*4

    elif num==2:
        # x축, y축 위의 점 추가 (큰 원 위의 점 포함)
        point = r*4 + 1
        for x in range(1, r):
            # 1사분면 위의 점 개수 * 4 (원 위의 점 포함)
            while x**2 + y**2 > r**2:
                y=y-1
            point+= y*4

    return point

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/181187#
