v = []

for i in range(4):
    v.append(int(input()))

def game_time(times: list = None):
    '''
    Args:
        times (list): The input contains four integer values representing
        the start time, start minute, end time, and end minute
    Return:
        time (str): The game time format e.g HH: mm 
    '''
    hour_start, min_start, hour_end, min_end = times

    if hour_end > hour_start:
        total_min = (hour_end - hour_start) * 60 + (min_end - min_start)
    else:
        total_min = (hour_end - hour_start + 24) * 60 + (min_end - min_start)

    hour = total_min // 60
    min = total_min - hour * 60

    return f'{hour}h{min}m'

print(game_time(times = v))