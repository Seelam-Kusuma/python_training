input_str= "Hello world and Hello Earth"
list_of_words=input_str.split()
d={}
for word in list_of_words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
    print(d)
   

