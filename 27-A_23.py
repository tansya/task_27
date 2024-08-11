def cost(lab):
    ct = 0
    x = A[lab][0] # ���������� ������ � ������������
    for i in range(0, n): # ���������� ��� ������
        dx = abs(x - A[i][0]) # ���������� �� ����������� �� ������ i
        ct += dx * A[i][1] # ��������� ��������� �� ������ i ����������� � ����� ���������
    return ct # ���������� ����� ���������

f = open('27_A_23.txt','r')
n = int(f.readline())
A = []
A = []
for i in range(n):
    r,pr = map(int,f.readline().split())
    A.append([r,(pr - 1) // 36 + 1]) # ������� ������ ���: ����������, ���������� �����������
ans = cost(0) #��������� ��������� ��� ������� ������
punkt = 0
for i in range(1,n):
    r = cost(i) # ��������� ��������� ��� ���������� ������ 
    if r < ans: # �������� ������
        ans = r
        punkt = i
print(punkt,ans)