# Operasi logika atau boolean

# Not, or, and, xor

#NOT
print('===NOT===')
a = False 
c = not a
print('data a =',a)
print('-------NOT')
print('data c =',c)

# OR (jika salah satu True, maka akan True)
print('===OR===')
a = False
b = False
c = a or b
print(a, 'OR',b,'=',c)
a = False
b = True
c = a or b
print(a, 'OR',b,'=',c)
a = True
b = False
c = a or b
print(a, 'OR',b,'=',c)
a = True
b = True
c = a or b
print(a, 'OR',b,'=',c)

# and (jika salah satu False, maka akan False)
print('===AND===')
a = False
b = False
c = a and b
print(a, 'AND',b,'=',c)
a = False
b = True
c = a and b
print(a, 'AND',b,'=',c)
a = True
b = False
c = a and b
print(a, 'AND',b,'=',c)
a = True
b = True
c = a and b
print(a, 'AND',b,'=',c)

# XOR (dia akan True jika salah satu True, sisanya False)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a, 'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a, 'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a, 'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a, 'XOR',b,'=',c)