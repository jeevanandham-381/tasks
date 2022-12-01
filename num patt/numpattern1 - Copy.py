rows=5
try:
    for i in range(rows,0,-1):
        for j in range(0,i+1):
            print(j,end=' ')
        print(' ')
finally:
    print('0')
