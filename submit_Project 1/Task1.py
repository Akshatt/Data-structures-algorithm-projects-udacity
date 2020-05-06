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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_text_no = set(i for j in texts for i in j[:2])
unique_call_no = set(i for j in calls for i in j[:2])
count = len(unique_text_no.union(unique_call_no))
print("There are {} different telephone numbers in the records.".format(count))