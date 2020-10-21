#list

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
lst3 = [11,12,13,14,15]

print(lst1)#print list 1
print(lst2)#print list 2
print(lst3)
print(lst1[1])# printing specified index

print(lst1[-3])# printing from last
print(lst1[0:2]) #printing in range
print(lst2[:3]) #print from to speciied index
print(lst1[2:])# print from specified index till end

#change list value
lst1[1] = 10
print(lst1)

#loop in list
for x in lst2:
  print(x)

#check item in list

if 9 in lst2:
    print("yes")

#list length

print(len(lst1))

#add item

lst2.append(11)
print(lst2)

lst1.insert(1, 6)
print(lst1)

#remove item

lst2.remove(9) #remove speciied item
print(lst2)

lst1.pop() #pop last index in list
print(lst1)

del lst1[1] #delete speciied index
print(lst1)

del lst1 #delete entire list

lst3.clear() #clear entire list

#copylist
lst4 = lst2.copy()
print(lst4)

lst5 = list(lst4)
print(lst5)

lst6= lst5 + lst2
print(lst6)

for x in lst5:
  lst6.append(x)#append method

print(lst6)

lst3.extend(lst5)
print(lst3)
