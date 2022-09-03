from random import  randint
def Mix(l):
    for i in range(len(l)*2):
        rnd1=randint(0,len(l)-1)
        rnd2=randint(0,len(l)-1)
        SwapElements(l,rnd1,rnd2)
def SwapElements(lis,i1,i2):
    temp=lis[i1]
    lis[i1]=lis[i2]
    lis[i2]=temp
l=list(range(1,10))
Mix(l)
print (l)