f = open('27_B_24.txt','r')
K = int(f.readline())
N =  int(f.readline())
A = list(map(int,f.readlines()))
f.close()
Pr = [-10 ** 9] * N # ���������� ������ ����������
Ps = [-10 ** 9] * N # ���������� ������ ����������
Pr[0] = A[0]
Ps[-1] = A[-1]
for i in range(N):
    Pr[i] = max(A[i],Pr[i - 1]) # ��������� ���������� ������ ����������
    Ps[-i - 1] = max(A[-i - 1],Ps[-i]) # ��������� ����������  ������ ����������
 
ans = A[0] + A[K] + A[2 * K] # ����� ������ ��������� ������
for i in range(K, N - K):
    ans = max(ans,A[i] + Pr[i - K] + Ps[i + K]) # �������� ������ �����
print(ans)
#17210