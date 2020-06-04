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

def generate(m, n):
    random_start = []
    random_stop = []
    for i in m:
        if i[0].isupper() or (i[0] == '"' and i[1].isupper()):
            random_start.append(i) 
        if i[-1] == '.' or i[-1] == '?' or i[-1] == '!':
            random_stop.append(i)

    for i in range(n):
        start_word = random.choice(random_start)
        curr_word = start_word
        answer = ""

        while curr_word not in random_stop:
            answer += curr_word
            answer += " "
            next_words = m[curr_word]
            r_next = random.choice(next_words)
            curr_word = r_next
        answer += curr_word
       
        print(answer, end="\n")


generate(mark, 5)