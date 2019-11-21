m=int(input())
for i in range(m,0,-1):
  for j in range(0,i):
    print('*',end=' ')
  print('\r')

for i in range(0,m,1):
  for j in range(0,i+1):
    print('*',end=' ')
  print('\r')
