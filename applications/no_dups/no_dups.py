def no_dups(s):
    # Your code here
    dups={}
    s_d=s.split()
    for word in s_d:
        if word not in dups:
            dups[word]=1
    return " ".join(list(dups.keys()))

        

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))