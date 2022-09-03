# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def GetSet(N):
    l=[];
    a=1
    for i in range(1,N+1):
        a=i*a
        l.append(a)
    return l
print(GetSet(4)) 