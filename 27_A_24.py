f = open('27_A_24.txt','r')
K = int(f.readline())
N =  int(f.readline())
A = list(map(int,f.readlines()))
sm = 0
for i in range(N):
    for j in range(i + K,N): # перебираем элементы на расстоянии не менее К от текущего 
        for g in range(j + K,N):
            sm = max(sm,A[i] + A[j] + A[g])
print(sm)
#189536            