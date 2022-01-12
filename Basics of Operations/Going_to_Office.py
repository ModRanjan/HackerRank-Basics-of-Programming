def onlineT(Distance):
    onlineP = int(O[0]) + (Distance - int(O[1])) * int(O[2])
    return onlineP

def classicT(Distance):
    classicP = int(C[1]) + ((Distance // int(C[0])) * int(C[2])) + (Distance * int(C[3]))
    return classicP

Distance = int(input())
O= list(input().split())
C= list(input().split())


# 13
# 6 7 4
# 4 2 1 2

onlineP = onlineT(Distance)
print(onlineP)
classicP = classicT(Distance)
print(classicP)

if onlineP > classicP:
    print("Online Taxi")
else:
    print("Classic Taxi")