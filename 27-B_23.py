f = open("27_B_23.txt",'r')
N = int(f.readline())
A = []
P = []#prefix forcount of containers
#first st not included in cost0 and  for prefix
s = f.readline().split()
x0 = int(s[0]) # ���������� ������� ������
prb= int(s[1]) # ���������� �������� ��� ������� ������
cont = (prb - 1) // 36 + 1 # ����������� ���������� ����������� ��� ������� ������
A.append([x0, cont]) # ��������� ������ ����� (� �������� 0)
P.append(cont) # ��������� ���������� ����������� � ���������� ������
st = 0
for i in range(1,N):  # ���������� ��������� ������ ��� ���� ������� 
    s = f.readline().split()
    x = int(s[0])
    prb= int(s[1])
    cont = (prb - 1) // 36 + 1
    A.append([x, cont])
    P.append(P[-1] + cont)
    st += (x - x0) * cont # ��������� ��� ������ � �������� 0
ans = 10 ** 18
for i in range(1,N):
    dx = A[i][0] - x0 # ���������� �� ����������� ������
    x0 = A[i][0] # ���������� ���������� �������� ������
    pos = P[i - 1]    # ���������� �����������, ��������� ������� �������������
    neg = P[N - 1] - P[i - 1] # ���������� �����������, ��������� ������� �����������
    st = st + dx * (pos - neg) # ��������� ���������, ���� ����������� � ������ i
    ans = min(st,ans) # �������� ������� ��������

print('ans', ans)
#ans 5634689219329 

