import re
name=input('enter your name:')
def mai():
  mail=input('enter your mail id:')
  if "@"in mail:
    if 'outlook'in mail or 'gmail' in mail:
      print('valid')
    else:
      print('invalid')
      mai()
  else:
    print('not in correct format')
    mai()
mai()
def mob():
  num=int(input('enter mob num:'))
  num=str(num)
  if len(num)==10:
    num=list(num)
    if num[0]=='9':
      print('valid')
    else:
      print('invalid')
      mob()
  else:
    print('not valid')
    mob()
mob()
def pin():
  while True:
    pin=input("enter pin:")
    if re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', pin):
      break
    else:
        print("incorrect")
        continue
pin()
balance=10000
while True:
  jk=int(input("User Choices 1.Deposit 2.Withdrawal 3.Balance  \nEnter your choice: "))
  if(jk==1):
    def deposit():
      try:
        n=int(input('enter the amount to add in your account:'))
        N=int(input('confirm the amount:'))
        if n==N:
          balance1=n+balance
          print(balance1)
        else:
          print('invalid')
          deposit()
      except:
        print('the amount should be in integer')
        deposit()
    deposit()
    break
  if(jk==2):
    def withdrawal():
      try:
        z=int(input('Enter the amount to withdraw from your account:'))
        ut=int(input('Confirm your amount:'))
        if z==ut:
          balan1=balance-z
          print('the balance in your acount:',balan1)
        else:
          print('invalid')
          withdrawal()
        def withd():
          w=balan1
          print(w)
      except:
        print('the amount should be in integer format')
        withdrawal()
  
    withdrawal()
    break
  if(jk==3):
    print('balance in your account:',balance)
    break

print('thank you for banking with us')
  
