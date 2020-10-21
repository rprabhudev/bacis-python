#dictionary
#changable
#indexed

dict1 ={
    "sport": "f1",
    "mode" : "track",
    "player":"verstappan",
    "crew" : "cobra"
}
print(dict1)

#access item by reering key value

x = dict1["mode"]
print(x)
#get method to access 
y = dict1.get("sport")
print(y)

#change value of specific item by refering to key

dict1["player"]="albon"
print(dict1)

#loop through dictionary
print("print key")
for x in dict1:
    print(x)#print key one by one
print("print value")
for x in dict1:
    print(dict1[x])#print values
print("print value using method")
for x in dict1.values():
    print(x)
print("print key and value using method")
for x,y in dict1.items():
    print(x,y)
#check if key exist
if "mode" in dict1:
    print("yes")
#length
print("length")
print(len(dict1))

#adding item
print("adding item")
dict1["team"] = "redbull"
print(dict1)

print("remove item")
dict1.pop("mode")#pop method
print(dict1)
print("pop item")
dict1.popitem()#pop last inserted item
print(dict1)

print("delete")
del dict1["crew"]
print(dict1)
"""
del dict1
this command can delete emtire dictionary

dict1.clear()
clear method will clear the entire dictionary
"""

#copy dictionary
print("copy dictionary")

dict2 =dict1.copy()#copy method
print("dict2", dict2)
dict3 ={
    "sport": "f1",
    "mode" : "track",
    "player":"bottas",
    "crew" : "enos"
}
dict4 = dict(dict3)
print("dict 4", dict4)   

#nested dictionary
print("nested doctionary")
f1 ={
    "team1":{
    "player" : "hamilton",
    "team" : "mercedes",
    "rank" : 1
    },
    "team2":{
    "player" : "bottas",
    "team" : "mercedes",
    "rank" : 2
    },
    "team3":{
    "player" : "verstappan",
    "team" : "redbull",
    "rank" : 3
    }
}
print(f1)
print("nesting already existing dictionary")

f2 ={
    "team4" : dict1,
    "team5" : dict3
}
print(f2)
