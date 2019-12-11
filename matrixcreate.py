R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
s=[]
for i in range(R):
  s1=[int(x) for x in input().split()][:R]
  s.append(s1)
print(s,end=' ')
