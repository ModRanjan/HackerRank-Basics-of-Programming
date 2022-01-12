time = input()
hh=int(time[:2])
mm = (hh*60)+ int(time[3:])
temp = 12/11*60
print(int(mm/temp+1))