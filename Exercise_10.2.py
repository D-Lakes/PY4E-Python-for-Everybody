# 10.2 
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dist = dict()
ordered = list()

for line in handle:
    line = line.rstrip()
    line = line.split()
    
    if len(line) < 1 or line[0] != 'From':
        continue
    else:
        time = list(line[5].split(':'))
        dist[time[0]] = dist.get(time[0], 0) + 1

for (k,v) in dist.items():
    tup = (k,v)
    ordered.append(tup)
    
ordered.sort()

for (k,v) in ordered:
    print(k,v)
