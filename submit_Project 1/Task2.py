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
dct = {}
for i in calls:
    if i[0] in dct.keys():
        dct[i[0]] += int(i[-1])
    else:
        dct[i[0]] = int(i[-1])
    if i[1] in dct.keys():
        dct[i[1]] += int(i[-1])
    else:
        dct[i[1]] = int(i[-1])
key = max(dct,key=dct.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, dct[key]))