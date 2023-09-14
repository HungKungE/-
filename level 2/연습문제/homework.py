def solution(plans):
    answer = []

    # 시작 시간기준 오름차순으로 sort
    plans = sorted(plans, key=lambda x : x[1])
    
    # [name, play_time]
    plan_stack = []
    
    cur_time = ""
        
    for new_plan in plans:
        while len(plan_stack)>0:
            # 이전 작업 종료 시간
            end_time = get_end_time(cur_time, plan_stack[-1][1])
            # 이전 작업이 안끝남 ( 이전 작업 끝나는 시간 > 이번 작업 시작시간)
            if end_time > new_plan[1]:
                plan_stack[-1][1] = get_minute(end_time, new_plan[1])
                break
            # 작업 끝 시간 == 작업 시작 시간 or
            # 작업2가 진즉에 끝남 (작업 끝 < 작업 시작)
            else:
                cur_time = end_time
                answer.append(plan_stack.pop()[0])
            
        # n번째
        if new_plan == plans[-1]:
            answer.append(new_plan[0])
            while len(plan_stack)>0:
                answer.append(plan_stack.pop()[0])
        # 1번째 ~ n-1번쨰
        else:
            cur_time=new_plan[1]
            plan_stack.append([new_plan[0],new_plan[2]])
        
    return answer

# 이 시간을 바꾸는 함수에서 계산 이후 다시 문자열로 바꿀때 각 시간, 분이 10 이하라면 버그가 생겼다.
# 의도한 값 : "08:00" -> 실제 값 : "8:0"
# 때문에 10 이하인지 확인하는 조건을 추가했다.
def get_end_time(time, playtimes):
    time_arr = [int(t) for t in time.split(":")]
    time_arr[1]+=int(playtimes)
    
    if time_arr[1] >= 60:
        time_arr[0] += time_arr[1]//60
        time_arr[1] = time_arr[1]%60

    hour=""
    minute=""
    
    if time_arr[0] < 10 :
        hour = "0"+str(time_arr[0])
    else:
        hour = str(time_arr[0])
    
    if time_arr[1] < 10 :
        minute = "0"+str(time_arr[1])
    else:
        minute = str(time_arr[1])
    
    return hour + ":" + minute
    
# 두 시간의 차이 ( 분으로 반환 )
def get_minute(end_time, new_time):
    # [시, 분]
    end_times = [int(i) for i in end_time.split(":")]
    new_times = [int(i) for i in new_time.split(":")]
    
    hour =  end_times[0]- new_times[0]
    minute = end_times[1]- new_times[1]
    
    # 둘의 부호가 같거나 둘 중 하나 이상이 0이면 그대로
    if (hour > 0 and minute > 0) or (hour < 0 and minute < 0) or hour == 0 or minute == 0:
        return str(abs(hour)*60 + abs(minute))
    # 둘의 부호가 다르면
    else:
        return str(abs(abs(hour)*60 - abs(minute)))


print(solution([["A", "08:00", "30"], ["B", "08:30", "20"], ["C", "08:50", "40"]]))
# 답 : ["A", "B", "C"]
print(solution([["A", "08:00", "30"], ["B", "08:30", "20"], ["C", "09:00", "30"], ["D", "09:30", "10"]]))
# 답 : ["A", "B", "C", "D"]
print(solution([["A", "08:00", "30"], ["B", "08:30", "20"], ["C", "09:00", "30"], ["D", "09:30", "10"], ["E", "10:00", "20"]]))
# 답 : ["A", "B", "C", "D", "E"]
print(solution([["A", "08:00", "30"], ["B", "08:30", "30"], ["C", "09:00", "30"]]))
# 답 : ["A", "B", "C"]

# 링크 - https://school.programmers.co.kr/learn/courses/30/lessons/176962