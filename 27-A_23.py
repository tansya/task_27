def cost(lab):
    ct = 0
    x = A[lab][0] # координата пункта с лабораторией
    for i in range(0, n): # перебираем все пункты
        dx = abs(x - A[i][0]) # расстояние до лаборатории от пункта i
        ct += dx * A[i][1] # стоимость перевозки от пункта i добавляется в общую стоимость
    return ct # возвращаем общую стоимость

f = open('27_A_23.txt','r')
n = int(f.readline())
A = []
A = []
for i in range(n):
    r,pr = map(int,f.readline().split())
    A.append([r,(pr - 1) // 36 + 1]) # создаем массив пар: координата, количество контейнеров
ans = cost(0) #вычисляем стоимость для первого пункта
punkt = 0
for i in range(1,n):
    r = cost(i) # вычисляем стоимость для очередного пункта 
    if r < ans: # выбираем лучший
        ans = r
        punkt = i
print(punkt,ans)