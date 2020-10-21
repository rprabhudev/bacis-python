#tuple
#imutable

tup1 = ("ford", "maserati","mercedes ", "audi", "volkswagen" )
tup2 = ("ferrari" , "redbull", "willams"," hass", "meclaren", "honda")


print(tup1)#print tuple 1
print(tup2)#print tuple 2

print(tup1[1])# printing specified index

print(tup1[-3])# printing from last
print(tup1[0:2]) #printing in range
print(tup2[:3]) #print from to speciied index
print(tup1[2:])# print from specified index till end



#loop in tuple
for x in tup2:
  print(x)

#check item in tuple

if "hass"in tup2:
    print("yes")

#tuple length

print(len(tup1))

#create tuple with one item
tup3 = ("alpha tuari" ,)# , will represnt tuple else will become string
print(tup3)

#remove item
del tup1 #delete entire tuple
#print(tup1)

#jointuple
tup4= tup2 + tup3
print(tup4)

