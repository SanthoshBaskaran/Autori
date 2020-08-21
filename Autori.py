a=input()
list1=[]
for j in a:
    list1.append(j)
s=''
s=s+a[0]
i=0
for i in list1:
    if(i=='-'):
        index1=list1.index(i)+1
        s=s+list1[index1]
        list1.remove(i)
print(s)
        
