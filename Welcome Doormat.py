n, m = map(int, input().split(' '))
p = m - 3
p = int(p/2)
n1 = int((n-1)/2)
k = int(((m-1)/2)-3)
j = 1
for i in range(n1):
    print('-'* p + '.|.' * j + '-' * p)
    p = p - 3
    j = j+2
print('-' * k + 'WELCOME' + '-' * k)

for i in range(n1):
    p = p + 3
    j = j - 2
    print('-'* p + '.|.' * j + '-' * p)
