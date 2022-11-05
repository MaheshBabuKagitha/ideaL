#AS-1
List=[]
for i in range (10,151):
    if i%5==0 and i%15==0:
        List.append(i)
print(List)

#AS-2
Prime=[]
for k in range (2,1000):
    if len(Prime)==100:
        break
    else:
        count=0
        for l in range (2,1000):
            if k%l==0:
                count+=1
        if count==1:
                Prime.append(k)

print(Prime,"\nHey Bro Done!")