"""
# int is pass by value
def majzoor(a):
    a = a ** 2

a = int(input("Lotfan add mored nazar ra vared konid : "))
majzoor(a)
print(a)
"""
# ***********************************************
"""
# float is pass by value
def majzoor(a):
    a = a ** 2

a = float(input("Lotfan add mored nazar ra vared konid : "))
majzoor(a)
print(a)
"""
# ***********************************************
"""
# List is pass by reference
def majzoor(a):
    a.append(a[0] ** 2)

a = [int(input("Lotfan add mored nazar ra vared konid : "))]
majzoor(a)
print(a)
"""
# ***********************************************
"""
# set is pass by reference
def majzoor(a):
    a = a ** 2
    b.add(a)

a = int(input("Lotfan add mored nazar ra vared konid : "))
b = set()
majzoor(a)
print(b)
"""
# ***********************************************
"""
# dictionary is pass by reference
def majzoor(a):
    a = a ** 2
    b['one'] = a

a = int(input("Lotfan add mored nazar ra vared konid : "))
b = {}
majzoor(a)
print(b)
"""
# ***********************************************

"""
# string is pass by value
def string(a):
    a = a + " Ezafe shode"

a = input("please write a string : ")
string(a)
print(a)
"""
# ***********************************************
"""
# tuple is pass by value
def majzoor(a):
    b = a**2

a = int(input("Lotfan add mored nazar ra vared konid : "))
b = ()
majzoor(a)
print(b)
"""

