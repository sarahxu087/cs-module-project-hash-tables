

def word_count(s):
    # Your code here
    s_c = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    for i in s_c:
        if i in s:
            s=s.replace(i,'')
    
    counts = {}
    new_s = s.split()
    for c in new_s:
        c=c.lower()
        if c in counts:
            counts[c]+=1
        else:
            counts[c] = 1
        
    items = dict(counts.items())
    return(items)

 
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))