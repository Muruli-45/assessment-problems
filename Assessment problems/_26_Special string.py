a=input()
s=input()
tot=0
for i in a:
    if i not in s:
        dist=9999
        for j in s:
            temp=abs(ord(i)-ord(j))
            if temp < dist:
                dist = temp
        tot += dist
print(tot)