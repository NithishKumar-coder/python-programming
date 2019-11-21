def armstrong():
  m=153
  w=len(m)
  o=0
  for i in range (0,w):
    u=int(m[i])
    o=o+(u**3)
  o=str(o)
  if o==m:
    print('yes')
  else:
    print('no')
armstrong()
