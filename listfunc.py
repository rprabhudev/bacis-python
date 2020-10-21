def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd +=1

    return even , odd

lst = [25,56,45,32,23,21,89,85,76,44]
even, odd = count(lst)
print("even: {} and odd :{}".format(even,odd))
