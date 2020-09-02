import re

def word_count(s):
    l = s.split()
    d = {}
    for i in range(len(l)):
        l[i] = l[i].lower()
        l[i] = l[i].translate({ord(c): "" for c in "\":;,.-+=/\\|[]{}()*^&"})
    for element in l:
        if element == '':
            d ={}
        else:
            d[element] = l.count(element)
    return d

    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count((('":;,.-+=/\\|[]{}()*^&'))))