list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
j=0
for i in list1:
    if i<0:
        list1.remove(i)
        continue
print(list1)
for j in list1:
    if j<0:
        list2.remove(i)
        continue
print(list2)
