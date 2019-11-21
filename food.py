def main():
  print('user name=',name)
  print('password=',password)
name=input()
password=int(input())
if password=='1234':
  u=input('enter the food you want')
  if u=='idli':
    g=int(input('how many do you want')
    if g<'0':
      t=g*10
      if t<100:
        print("your charge is:",t)
      else:
        y=t*150
        print('your charge is',y)
    else:
      print('cannot place the order')
  elif  u=='dosa':
    g=int(input('how many do you want')
    if g>0:
      t=g*30
      if t<100:
        print("your charge is:",t)
      else:
        y=t*150
        print('your charge is',y)
    else:
      print('cannot place the order')
  elif u=='poori':
    g=int(input('how many do you want')
    if g>0:
      t=g*50
      if t<100:
        print("your charge is:",t)
      else:
        y=t*150
        print('your charge is',y)
    else:
      print('cannot place the order')
  elif u=='pizza':
    g=int(input('how many do you want')
    if g>0:
      t=g*150
      if t<100:
        print("your charge is:",t)
      else:
        y=t*150
        print('your charge is',y)
    else:
      print('cannot place the order')
  else:
    print('we dont have the item;)
else:
  print('invalid password')
