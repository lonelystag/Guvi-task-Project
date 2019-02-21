n = int(input())
L = []
for i in range(1,n+1):
    L.append(str(i))
    print (''.join(L)+''.join(L[::-1][1:]))
