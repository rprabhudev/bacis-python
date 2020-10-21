#looping statements
print("while loop")

x = int(input("enter a number"))
i = 0
while i<x:
    print("while statement true",i)
    i+=1
print("while loop ended")

#break

j=1
while j<x:
    print("while true",j)
    if(j==3):
        break #break the loop
    j+=1


j=1
while j<x:
    j+=1
    if(j==3):
        continue #continue  the loop
    print("while loop true", j)
print("while else")
i=0
while i<6:
    print("while true",i)
    i+=1
else:
    print("while condtion failed ")

print("for loop")

team = ["redbull", "apla tuari","willaims", "haas"]
player = ["max", "gas", "kim", "lat"]
for x in team:
    print(x)
for x in "roger federer":
    print(x)#loop through string
print("break")
for x in player:
    print(x)
    if x== "kim":
        break #break the loop and exit
print("continue")
for x in team:
    if x== "alpha tuari":
        continue #continue the loop
    print(x)
print("range set to 10")
for x in range(10):
    print(x)
print("range set between 5-10")
for x in range(5,10):
    print(x)
print("range set between 1-30 and increment set to 3")
for x in range(1,30,3):#range with increment
    print(x)
#nested for
for x in team:
    for y in player:
        print(x,y)
