n=5
m=(2*n)-2
for i in range(0,n):
  for j in range(0,m):
    print(end=" ")
  m=m-1
  for j in range(0,i):
    if i%2!=0:
      print('*',end=' ')
  print(" ")
for q in range(n,0,-1):
  for w in range(0,m): 
    print(end=' ')
  m=m+1
  for w in range(0,q):
    if q%2!=0:
      print('*',end=' ')
  print(' ')
