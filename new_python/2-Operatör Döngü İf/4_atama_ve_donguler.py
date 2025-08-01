# =====================================================
# Atama Operatörleri ve Temel Döngüler
# =====================================================

# Atama işlemleri
x, y, z = 2, 5, 10
values = 1, 2, 3, 4, 5
print(values)
print(type(values))
x, y, *z = values
print(x, y, z)
print(x, y, z[1])

# for döngüsü örnekleri
numbers = [1,2,3,4,5]
for a in numbers:
    print('Hello')
names = ['çınar','sadık','sena']
for name in names:
    print(f'my name is {name}')
name = 'Sadık Turan'
for n in name:
    print(n)
tuple_list = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple_list:
    print(a,b)
d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(key, value)


# while döngüsü örneği
x = 1
while x <= 100:
    if x % 2==1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1
print('bitti...')
