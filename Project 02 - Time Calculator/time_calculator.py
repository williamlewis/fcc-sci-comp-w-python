"""
- accept inputs:  start time, duration, (optional) day of week
- add duration to start time by breaking each into hours & minutes, and get AM/PM from start time
- if hours go over 12, subtract 12 & change b/w AM & PM
    - figure out how to handle multiple days (for any hour whole num in duration)
- if minutes go over 60, subtract 60 & add 1 to hour (should process mins before hrs)
- if suffix changes from PM to AM, change day to next in week, & add note for for next day or n days later
- one space between response parts, comma after result time if followed by a day of the week
"""


test_input = ["11:30 AM", "2:32", "Monday"]

start = test_input[0]
duration = test_input[1]
day = None
if len(test_input) > 2:
    day = test_input[2]


#----------------

# break start time and duration inputs into component parts
start_hrs = int(start.split(':')[0])
start_mins = int(start.split(':')[1][:2])
start_ampm = start[-2:]
start_day = day

dur_hrs = int(duration.split(':')[0])
dur_mins = int(duration.split(':')[1])


# do basic math to add duration to start time
res_hrs = start_hrs + dur_hrs
res_min = start_mins + dur_mins
res_ampm = start_ampm # set as original, to remain unless changed


# make time conversions to handle spilling over into next hour, into next AM/PM cycle, into next day, or into subsequent days
# convert minutes to roll over into next hour
if res_min > 59:
    res_min -= 59
    if res_min < 10:
        res_min = '0' + str(res_min)
    res_hrs += 1

# convert between AM and PM, then handle roll over to following day (not multiple days)
if (res_hrs > 12) and (res_hrs < 24):
    res_hrs -= 12
    if start_ampm == 'AM':
        res_ampm = 'PM'
    elif start_ampm == 'PM':
        res_ampm = 'AM'
        print('trigger day change here')
        # handle SINGLE day conversion here...
    else:
        print('error changing b/w AM and PM')

# convert between AM and PM, then handle roll over for multiple days ahead
# consider making am/pm conversion a small function to put in both blocks here








res_time = str(res_hrs) + ':' + str(res_min) + ' ' + res_ampm

# print(start_hrs)
# print(start_mins)
# print(start_ampm)
# print(day)
# print(dur_hrs)
# print(dur_mins)
# print(res_hrs)
# print(res_min)
print(res_time)


# start_ampm = ''
# start_hrs = ''
# start_mins = ''
# start_day = ''

# dur_hrs = ''
# dur_mins = ''

# res_hrs = ''
# res_mins = ''
# res_ampm = ''
# res_day = ''
