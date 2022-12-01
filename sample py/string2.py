text=input()
ans="abcdefghijklmnopqrstuvwxyz"
ans1=""
n=len(text)
for i in range n:
    while(text[i] not in ans):
        ans1+=txet[i]
print(ans1)
