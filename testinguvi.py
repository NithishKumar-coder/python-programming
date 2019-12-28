d=input()
l=[]
l2=[]
l3=[]
for i in d:
  q=ord(i)
  l.append(q)
for i in l:
  if i==97 or i==101 or i==105 or i==111 or i==117:
    aa=i-1
    l2.append(aa)
  else:
    sss=i+1
    l2.append(sss)
for i in l2:
  w=chr(i)
  l3.append(w)
print("".join(l3))
