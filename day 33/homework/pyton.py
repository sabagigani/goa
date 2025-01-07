def split(line,delim):
    s=[]
    j=0
    for i in range (len(line)-1):
        if delim== line [i]:
            s.append(line[j:i])
            j=i+1
    s.append (line[j:])
    return s

original_string = "Hello, World!"
modified_string = original_string.replace("Hello", "Welcome")

