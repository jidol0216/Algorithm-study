def fk(cb):
    total =0
    for sb in range(0,3,1):
        total += cb[sb]
    cb[2]= total
    return cb

ca =[10,20,30]
print(ca)
cd = fk(ca)
print(type(cd))

print(ca)
print(cd)