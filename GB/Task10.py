#Найти расстояние между двумя точками пространства
def GetDistance(point1,point2):
    return ((point2[0]-point1[0])**2+(point2[1]-point1[1])**2+(point2[2]-point1[2])**2)**0.5
point1=[10,15,20]
point2=[50,10,30]

print(GetDistance(point1,point2))




