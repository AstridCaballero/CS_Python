def h(y):
    print(id(y))
    z = x is y
    print(z)
    # x.append(1)
    y = [0, 1]
    print (id(y))
    t = x is y
    print(t)
    print(x) 
    
    return x

x = [0]
print(id(x))
h(x)
print(x)
# print(h(x))