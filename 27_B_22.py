f = open('27_B_22.txt','r')
P = [0] #������� ���������� ������ � ������������ ������� ���������
N = int(f.readline()) # ��������� ���������� ��������� � ������������������
for i in range(N):
    x = int(f.readline()) # ��������� �� ������ ��������� ��������
    P.append(P[-1] + x) # ��������� � ��������� ������ ����� ��������
f.close()
A = [0] * 43 # ������� �������������� ������, � ������� �������� ������������� �������  
mx_sm = 0 # ������������ �����
ans = 0 # ����� - ��������� ����� �������������������� � ������������ ������
for i in range(1,len(P)):
    mod = P[i] % 43 # ������� ��� �������� �������� ����������� �������
    if mod != 0: # ������� ������� ��� ���������
        if A[mod] == 0: # ������� ���������� �������
            A[mod] = [P[i],i] # ��������� ��� ������� ��������� ���� �������
        else: 
            if P[i] - A[mod][0] > mx_sm: # ��� ����������� �������� ��������� ������ �����
                mx_sm = P[i] - A[mod][0] # ������ ������ �����
                ans = i - A[mod][1] # ���������� ����� ����� ��� ������ �����
            elif P[i] - A[mod][0] == mx_sm: # � ������ ��������� ������ �����
                ans = min(ans, i - A[mod][1]) # �������� ������ �����
    else:
        mx_sm = P[i] # ��� �������� ������� ����� � ����� ������ ���������
        ans = i # ��������� ������ �����
print(ans)
#ans = 329329
