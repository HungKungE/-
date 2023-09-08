def solution(id_list, report, k):
    answer = []
    
    user_dict = {id_list[i]:[] for i in range(len(id_list))}
    reported_count_dict = {id_list[i]:0 for i in range(len(id_list))}
    user_mail_dict = {id_list[i]:0 for i in range(len(id_list))}
    
    for rep in report:
        report_log = rep.split(" ")
        if report_log[1] not in user_dict[report_log[0]]:
            user_dict[report_log[0]].append(report_log[1])
            reported_count_dict[report_log[1]] += 1
    
    for key, value in reported_count_dict.items():
        if value >= k:
            for key2, value2 in user_dict.items():
                if key in value2:
                    user_mail_dict[key2] += 1
    
    for i in user_mail_dict.values():
        answer.append(i)
    
    return answer