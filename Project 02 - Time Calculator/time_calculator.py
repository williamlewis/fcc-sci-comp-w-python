"""
/ accept inputs:  start time, duration, (optional) day of week
/ add duration to start time by breaking each into hours & minutes, and get AM/PM from start time
/ if hours go over 12, subtract 12 & change b/w AM & PM
    - figure out how to handle multiple days (for any hour whole num in duration)
/ if minutes go over 60, subtract 60 & add 1 to hour (should process mins before hrs)
/ if suffix changes from PM to AM, change day to next in week, & add note for for next day or n days later
/ one space between response parts, comma after result time if followed by a day of the week
"""


# test_input = ["3:00 PM", "3:10"]
    # Returns: 6:10 PM  

# test_input = ["11:30 AM", "2:32", "Monday"]
    # Returns: 2:02 PM, Monday

# test_input = ["11:43 AM", "00:20"]
    # Returns: 12:03 PM

# test_input = ["10:10 PM", "3:30"]
    # Returns: 1:40 AM (next day)

# test_input = ["11:43 PM", "24:20", "tueSday"] # NOT WORKING, not getting from 11 to 12, 1 day too many in rollover
    # Returns: 12:03 AM, Thursday (2 days later)

test_input = ["6:30 PM", "205:12"] # NOT WORKING, not switching from PM to AM
    # Returns: 7:42 AM (9 days later)




days_of_wk = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

start = test_input[0]
duration = test_input[1]
day = None
days_later = 0
day_index = -1 # placeholder value, out of possible range
if len(test_input) > 2:
    day = test_input[2]
    day = day.lower()
    day = day.capitalize()
    day_index = days_of_wk.index(day)



def change_ampm(start_ampm):
    # for res_hrs between 12 and 24; changes between AM & PM, then flags if time rolls into next day
    if start_ampm == 'AM':
        res_ampm = 'PM'
        add_day = False
    elif start_ampm == 'PM':
        res_ampm = 'AM'
        add_day = True
    else:
        print('Error changing b/w AM and PM')
    return res_ampm, add_day



# break start time and duration inputs into component parts
start_hrs = int(start.split(':')[0])
start_mins = int(start.split(':')[1][:2])
start_ampm = start[-2:]
start_day = day

dur_hrs = int(duration.split(':')[0])
dur_mins = int(duration.split(':')[1])


# do basic math to add duration to start time
res_hrs = start_hrs
res_min = start_mins + dur_mins
res_ampm = start_ampm # set as original, to remain unless changed
res_day = start_day # set as original, to remain unless changed



# make time conversions to handle spilling over into next hour, into next AM/PM cycle, into next day, or into subsequent days
# convert minutes to roll over into next hour
if res_min > 59:
    res_min -= 60
    if res_min < 10:
        res_min = '0' + str(res_min)
    
    res_hrs += 1
    if res_hrs == 12:
        res_ampm, add_day = change_ampm(start_ampm)

        if add_day is True:
            days_later += 1
            #day_index += 1 CONFLICTING BY DOUBLING UP W/ INCREMENT IN 24+ CODE BLOCK BELOW

print(res_hrs)
print(res_min)
print(res_ampm)


days_later += dur_hrs // 24
res_hrs += dur_hrs % 24
if res_hrs > 24:
    days_later += res_hrs // 24
    res_hrs += res_hrs % 24


        # if res_hrs > 24: # has to be repeated one time, in case extra hours plust start time go over 24
        #     days_later += res_hrs // 24
        #     extra_hours = res_hrs % 24

        #     res_hrs = start_hrs + extra_hours

    # while res_hrs > 24:
    #     days_later += res_hrs // 24
    #     print(str(days_later) + ' days later')
    #     extra_hrs = res_hrs % 24
    #     print(str(extra_hrs) + ' extra hours')
    #     #day_index += days_later

    #     res_hrs -= 24
    #     # ...........go back to adding extra hours (from modulus) to start time?
    
    # res_hrs = start_hrs + extra_hrs



if 12 < res_hrs < 24: # make a while loop
    res_hrs -= 12
    res_ampm, add_day = change_ampm(start_ampm)

    # TEST TO REINSTATE
    if add_day is True:
        days_later += 1
        #day_index += 1


res_time = str(res_hrs) + ':' + str(res_min) + ' ' + res_ampm
if res_hrs <= 12:
    res_time = str(res_hrs) + ':' + str(res_min) + ' ' + res_ampm



day_index += days_later
if day_index > 6:
    while day_index > 6:
        day_index -= 7
res_day = days_of_wk[day_index]


if day is None:
    if days_later == 0:
        pass
    elif days_later == 1:
        res_time += ' (next day)'
    elif days_later > 1:
        res_time += ' (' + str(days_later) + ' days later)'
    else:
        print('error calculating days later WITHOUT day of week')
elif day is not None:
    if days_later == 0:
        res_time += ', ' + str(res_day)
    elif days_later > 0:
        res_time += ', ' + str(res_day) + ' (' + str(days_later) + ' days later)'
    else:
        print('error calculating days later WITH day of week')
else:
    print('error calculating day')


print(res_time)






















'''
# handle roll over to NEXT day (not multiple days), using change_ampm function
if (res_hrs > 12) and (res_hrs < 24):
    res_hrs -= 12
    res_ampm, add_day = change_ampm(start_ampm)

    if add_day == True:
        day_index += 1

# handle roll over for MULTIPLE days ahead, also using change_ampm function
elif res_hrs > 24:
    days_later = res_hrs // 24
    extra_hrs = res_hrs % 24
    res_hrs = start_hrs + extra_hrs
    
    if res_hrs > 24:
        days_later = res_hrs // 24
        extra_hrs = res_hrs % 24
        res_hrs = start_hrs + extra_hrs

    
    elif (res_hrs > 12) and (res_hrs < 24):
        res_hrs -= 12
        res_ampm, add_day = change_ampm(start_ampm)

        if add_day == True:
            days_later += 1
            day_index += days_later
    else:
        print('problem trying to work hours down to 12 hours')


else:
    print('problem trying to convert time')



    # break down in to 24hr cycles, to get # days later
    # add extra hours to convert to am/pm
    # still check for next day out of am/pm function, and add an ADDITIONAL day to # days later if it goes from PM to AM
'''







'''
FUNCTIONS TO BUILD:

- change_ampm
    call if result hours are between 12 & 24
    return:
        new AM/PM value
        new day true or false (i.e. next day)




- convert_days
    call if result hours are over 24
    retun:
        number of FULL days later (floor division)
        number of extra hours (modulus division)



- check for full days forward at same time (for res_hrs 24 & above)
- check for AM/PM change 




def check_days_ahead():
- for res_hrs 24+, check for number of full days forward + extra hours

def check_am_pm():
- for res_hrs between 12 & 24, convert back to 12 hour format & handle AM/PM switch

def check_day_rollover:
- for PM to AM conversion, trigger next day















handle minutes to stay under 60, add 1 to hour if rolling over

check for over 24 hours (multi-day rollover)
check again for over 24 hours, in case extra hours 
    make function take care of all of it?

    calculate which next day, for one-day rollover to add onto

check for over 12 hours, to switch AM/PM and trigger one day rollover (alone or on top of multi-day)

format output





for calculating day of week
    list for ordered indices of each day
    if list index goes over 6 (7th day), subtract 7 to go back through
    just loop through to increment index & output result index value

'''

