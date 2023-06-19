a=input("enter a five letter word:-")
ascii_values=[]
str1=' '
for c in a:
    print(c)
    ascii_values.append(ord(c))
print(ascii_values)
for i in ascii_values:
    b=i-30
    str1+=chr(b)
    print(chr(b))
print(str1)