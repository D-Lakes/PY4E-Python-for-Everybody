# 9.4 
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

senders = dict()
largest_value = -1
largest_key = None
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.split()
    if len(line) < 2 or line[0] != "From":
        continue
    else:
        senders[line[1]] = senders.get(line[1],0) + 1
for k,v in senders.items():
    if v > largest_value:
        largest_value = v
        largest_key = k
print(largest_key, largest_value) 