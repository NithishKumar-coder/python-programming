def mains():
    name=input()
    ph=input()
    email=input()
mains()
distance=int(input())

def fun():
    mot=input()
    if mot=='car':
        fair=distance*30
        print(fair)
        return fair
    elif mot=='auto':
        fair=distance*20
        print(fair)
        return(fair)
    elif mot=='bike':
        fair=distance*10
        print(fair)
        return(fair)
    else:
        return'not available'
    
fun()
print('is price affordable')
a=input()
list=[]
if a=='yes':
    print('thanks')
    list.append(mains())
else:
    fun()




     
