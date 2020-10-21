#set
#unordered

st1 = {"roger", "nadal","stan","del","monfil","andre"}
st2 = {"ham","bot","ver","alb","nor","ric"}
st3 = {"lec","hul","vet","sai","lat","sch"}

print(st1)#print set 1
print(st2)#print set 2
print(st3)

#cannot change set value

#loop in set
print("printing in for loop")
for x in st2:
  print(x)

#check item in set
print("check item ver in set 2")
if "ver" in st2:
    print("yes")


#add item

st2.add("mas")# add one item
print(st2)

st1.update(["spunk","cosco","nike"])#add multiple item
print(st1)
#set length

print(len(st1))

#remove item

st3.remove("hul") #remove speciied item ,if item dosent exist error 
print(st3)

st2.discard("ham") #remove speciied item ,even if item dosent exist no error 
print(st2)
#pop last index in set but set is un ordered so we cannot determine the item
x=st1.pop() 
print(x)
st3.clear() #clear entire set

del st3 #delete set completely
#print(st3)

#join two sets
st4 = st1.union(st2)
print(st4)

st5 = {"cobra","neos","redbull","pirelli"}
st5.update(st2)
print(st5)
