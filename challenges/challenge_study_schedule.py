def study_schedule(start_time, end_time, target_time):
    if target_time == 0:
        return 0
    students_qtd = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time and target_time <= end_time[index]:
            students_qtd += 1
    return students_qtd
