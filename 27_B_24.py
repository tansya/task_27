f = open('27_B_24.txt','r')
K = int(f.readline())
N =  int(f.readline())
A = list(map(int,f.readlines()))
f.close()
Pr = [-10 ** 9] * N # префиксный массив максимумов
Ps = [-10 ** 9] * N # суффиксный массив максимумов
Pr[0] = A[0]
Ps[-1] = A[-1]
for i in range(N):
    Pr[i] = max(A[i],Pr[i - 1]) # заполняем префиксный массив максимумов
    Ps[-i - 1] = max(A[-i - 1],Ps[-i]) # заполняем суффиксный  массив максимумов
 
ans = A[0] + A[K] + A[2 * K] # сумма первой возможной тройки
for i in range(K, N - K):
    ans = max(ans,A[i] + Pr[i - K] + Ps[i + K]) # выбираем лучшую сумму
print(ans)
#17210