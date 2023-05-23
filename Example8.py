n= input('Введите длинну плитки:')
m= input('Введите ширину плитки:')
k= input('Введите кол-во долек котоыре хотите отломить:')
n = int (n)
m = int (m)
k = int (k)
if k%n==0 or k%m==0:
    print( n, 'x', m ,' / ', k,'--> yes')
else:
    print( n, 'x', m ,' / ', k,'--> no')