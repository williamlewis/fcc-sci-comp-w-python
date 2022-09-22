def add_time(start, duration, day=None):

    days_of_wk = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_later = 0
    if day is not None:
        day = day.lower()
        day = day.capitalize()
        day_index = days_of_wk.index(day)
    
    
    def change_ampm(start_ampm):
        # converts between AM and PM for hour values over 12 and also flags if time rolls into next day
        if start_ampm == 'AM':
            res_ampm = 'PM'
            add_day = False
        elif start_ampm == 'PM':
            res_ampm = 'AM'
            add_day = True
        else:
            print('Error changing between AM and PM.')
        return res_ampm, add_day
    
    
    # break start time and duration inputs into component parts
    start_hrs = int(start.split(':')[0])
    start_mins = int(start.split(':')[1][:2])
    start_ampm = start[-2:]
    start_day = day
    
    dur_hrs = int(duration.split(':')[0])
    dur_mins = int(duration.split(':')[1])
    
    
    # do basic math to add duration to start time (minutes first)
    res_hrs = start_hrs # set original as default value
    res_min = start_mins + dur_mins
    res_ampm = start_ampm # set original as default value
    res_day = start_day # set original as default value
    
    
    # make time conversions to handle spilling over into next hour, into next AM/PM cycle, into next day, or into subsequent days
    # convert minutes to roll over into next hour
    if res_min > 59:
        res_min -= 60
                
        res_hrs += 1
        if res_hrs == 12:
            res_ampm, add_day = change_ampm(start_ampm)
    
            if add_day is True:
                days_later += 1
    
    if res_min < 10:
            res_min = '0' + str(res_min) # format for final output
    
    # convert durations over 24 hours into multiple days later
    days_later += dur_hrs // 24
    res_hrs += dur_hrs % 24
    if res_hrs > 24:
        days_later += res_hrs // 24
        res_hrs += res_hrs % 24
    
    
    # convert to 12-hour time format if value is in P.M. range
    if 12 < res_hrs < 24:
        res_hrs -= 12
        res_ampm, add_day = change_ampm(start_ampm)
    
        if add_day is True:
            days_later += 1
    
    
    # calculate day of the week based on number of days later
    if day is not None:
        day_index += days_later
        if day_index > 6:
            while day_index > 6:
                day_index -= 7
        res_day = days_of_wk[day_index] # retrieve day of week from list variable
    
    
    # format basic output
    if res_hrs <= 12:
        res_time = str(res_hrs) + ':' + str(res_min) + ' ' + res_ampm
    else:
        print('Error calculating hour into 12-hour format.')
    
    
    # modify output to include day of week and number of days ahead, as applicable
    if day is None:
        if days_later == 0:
            pass
        elif days_later == 1:
            res_time += ' (next day)'
        elif days_later > 1:
            res_time += ' (' + str(days_later) + ' days later)'
        else:
            print('Error calculating number of days later WITHOUT day of week.')
    elif day is not None:
        if days_later == 0:
            res_time += ', ' + str(res_day)
        elif days_later == 1:
            res_time += ', ' + str(res_day) + ' (next day)'    
        elif days_later > 1:
            res_time += ', ' + str(res_day) + ' (' + str(days_later) + ' days later)'
        else:
            print('Error calculating number days later WITH day of week.')
    else:
        print('Error calculating day output.')
    
    
    new_time = res_time

    return new_time
  