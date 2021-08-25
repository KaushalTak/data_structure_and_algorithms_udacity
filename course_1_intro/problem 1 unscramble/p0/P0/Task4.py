"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def text_senders_receivers(texts):
    temp = []
    for detail in texts:
        temp += detail[:2]
    return set(temp)

def callers_receivers(calls):
    callers = []
    receivers = []
    for detail in calls:
        callers.append(detail[0])
        receivers.append(detail[1])
    return set(callers), set(receivers)

def possible_telemarketers(calls, texts):
    texters = text_senders_receivers(texts)
    callers, receivers = callers_receivers(calls)
    non_tele = texters.union(receivers)
    telemarketers = callers.difference(non_tele)
    return sorted(list(telemarketers))

def answer(calls, texts):
    print("These numbers could be telemarketers: ")
    for num in possible_telemarketers(calls, texts):
        print(num)

answer(calls, texts)
