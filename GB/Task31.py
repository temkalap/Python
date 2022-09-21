# Составить список простых множителей натурального числа N

def GetSimpleMultipliers(n):
    lst = []
    lstofMulty = [2, 3, 5, 7]
    for i in lstofMulty:
        flag = True
        while flag:
            if n % i == 0:
                n = int(n / i)
                lst.append(i)
            else:
                flag = False
    if n != 1:
        lst.append(n)
    return lst


print(GetSimpleMultipliers((256)))
