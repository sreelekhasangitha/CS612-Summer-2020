a = 10
b = 20

list = [1,2,3,4,5]

if a in list:
    print ("Line 1 - a and b have same identity")
else:
    print ("Line 1 - a and b do not have same identity")

if (id(a) == id(b)):
    print ("Line 2 - a and b have same identity")
else: 
    print ("Line 2 - a and b do not have same identity")

b = 30

if (a is b):
    print ("Line 3 - a and b have same identity")
else: 
    print ("Line 3 - a and b do not have same identity")

if (a is not b):
    print ("Line 4 - a and b have same identity")
else:
    print ("Line 4 - a and b do not have same identity")