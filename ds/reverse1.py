# input=one two three,output=three two one

s1 = input("enter your string:")
rev = s1.split()[::-1]
l = []
for i in rev:
    l.append(i)
print(" ".join(l))
