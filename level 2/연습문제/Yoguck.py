def solution(targets):
    answer = 0
    shoot = -1
    
    targets.sort()
    
    #print(targets)
    
    for target in targets:
        if target[0]>shoot:
            shoot=target[1]-0.5
            answer+=1
        else:
            if target[1] < shoot:
                shoot=target[1]-0.5

    return answer


#### 설명
'''
1. 설명

미사일은 x좌표 (s, e)로 표시 된다. s ~ e 범위가 미사일 위치이다.

미사일의 머리와 끝이 아닌, 몸체를 맞춰야 요격된다.

수많은 미사일이 날아 올 때, 이를 요격하기 위해 레이저를 발사한다. ( 직선 공격 )

이 때, 모든 미사일을 요격하는 레이저 최소 발사 횟수는?

2. 풀이

- 레이저를 발사하는 x좌표(shoot)를 -1로 초기화한다.

- 미사일 위치 리스트(targets)를 오름차순으로 정렬한다.

- 미사일 1개(target)의 시작 위치(target[0])보다 shoot을 비교
  1. target[0] > shoot
  레이저 발사 위치를 미사일의 끝 위치(target[1])-0.5로 이동한다. ( 그래야 미사일 요격 가능 )
  그리고 레이저 발사 횟수를 증가시킨다.
  
  2. target[0] < shoot
  이전 미사일보다 시작 위치는 높지만 끝 위치가 작다.
  따라서 현재 미사일의 끝 위치와 shoot을 비교해야한다.
  
    1) target[1] < shoot
    현재 미사일의 끝 위치도 이전 미사일들의 끝 위치보다 작기 때문에
    현재 미사일과 이전 미사일들이 겹쳐 있음을 알 수 있다.
    따라서 미사일들을 한번에 격추시키기 위해 레이저 발사 위치를 현재 미사일 끝 위치 - 0.5로 변경한다.
    
    2) target[1] > shoot
    현재 미사일이 충분히 길기 때문에 레이저 발사 위치를 바꾸지 않아도 한번에 요격 가능하다.
'''