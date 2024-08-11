f = open("27_B_23.txt",'r')
N = int(f.readline())
A = []
P = []#prefix forcount of containers
#first st not included in cost0 and  for prefix
s = f.readline().split()
x0 = int(s[0]) # координата первого пункта
prb= int(s[1]) # количество пробирок для первого пункта
cont = (prb - 1) // 36 + 1 # необходимое количество контейнеров для первого пункта
A.append([x0, cont]) # добавляем первый пункт (с индексом 0)
P.append(cont) # добавляем количество контейнеров в префиксный массив
st = 0
for i in range(1,N):  # аналогично созраняем двнные для всех пунктов 
    s = f.readline().split()
    x = int(s[0])
    prb= int(s[1])
    cont = (prb - 1) // 36 + 1
    A.append([x, cont])
    P.append(P[-1] + cont)
    st += (x - x0) * cont # стоимость для пункта с индексом 0
ans = 10 ** 18
for i in range(1,N):
    dx = A[i][0] - x0 # расстояние до предыдущего пункта
    x0 = A[i][0] # запоминаем координату текущего пункта
    pos = P[i - 1]    # количество контейнеров, стоимость которых увеличивается
    neg = P[N - 1] - P[i - 1] # количество контейнеров, стоимость которых уменьшается
    st = st + dx * (pos - neg) # стоимость перевозок, если лаборатория в пункте i
    ans = min(st,ans) # выбираем меньшее значение

print('ans', ans)
#ans 5634689219329 

