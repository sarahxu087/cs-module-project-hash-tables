# Your code here
with open("robin.txt") as f:
    words = f.read()

s_c = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

for i in s_c:
     if i in words:
        s=s.replace(i,'')
    
counts = {}
new_s = s.split()