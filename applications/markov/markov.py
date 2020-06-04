import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
words = words.split()
print(words)
mark={}
# TODO: analyze which words can follow other words
# Your code here
for i in range(len(words)-1):
    if words[i] not in mark:
        mark[words[i]]=[]
        mark[words[i]].append(words[i+1]) 
    else:
        mark[words[i]].append(words[i+1])
   
print(mark)

# TODO: construct 5 random sentences
# Your code here

