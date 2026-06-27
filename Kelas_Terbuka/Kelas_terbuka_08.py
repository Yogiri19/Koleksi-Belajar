# Operasi aritmatika
a = 10
b = 3

#Oprasi tambah +
hasil = a + b
print(a,'+',b,'=', hasil)

#Operasi pengurangan  -
hasil = a - b
print(a,'-',b,'=', hasil)

#Operasi Perkalian  *
hasil = a * b
print(a,'*',b,'=', hasil)

#Operasi pembagian  /
hasil = a / b
print(a,'/',b,'=', hasil)

#Operasi eksponen  ** (ini adalah perpangkatan)
hasil = a ** b
print(a,'**',b,'=', hasil)

#Operasi modulus  % (sisa pembagian)
hasil = a % b
print(a,'%',b,'=', hasil)

#Operasi floor division  // (pembulatan dari pembagian)
hasil = a // b
print(a,'//',b,'=', hasil)

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman *,/,**,%,//
    4. pertambahan dan pengurangan +,-
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)
 
hasil = x + y * z
print(x,'+',y,'*',z, '=',hasil)
# kurung akan mengambil langkah paling pertama diantara paling pertama 
hasil = (x + y) * (z + y)
print('(',x,'+',y,') * (',z, '+',y,') =',hasil)