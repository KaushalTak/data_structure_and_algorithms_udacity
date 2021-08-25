"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def get_call_durations(calls):
    temp_dict = {}
    for detail in calls:
        temp_dict[detail[0]] = temp_dict.get(detail[0], 0) + int(detail[3])
        temp_dict[detail[1]] = temp_dict.get(detail[1], 0) + int(detail[3])
    return temp_dict

def who_is_always_on_call(calls):
    temp_dict = get_call_durations(calls)
    max_num = max(temp_dict, key = lambda k: temp_dict[k])
    max_duration = temp_dict[max_num]
    return max_num, max_duration

talkitive, duration = who_is_always_on_call(calls)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(talkitive, duration))