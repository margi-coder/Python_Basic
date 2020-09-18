#27. Python Arithmetic Operators

x = 7
y = 2

print("x = {} , y = {} ".format(x,y))
print("Addition x + y = {}".format(x+y))
print("Substraction x - y = {}".format(x-y))
print("Multiplication x * y = {}".format(x*y))
print("Multiplication to string,  \"hello \" * y = {}".format('hello '*y))
print("Division x / y = {}".format(x/y))
print("Power/pow x ** y = {}".format(x**y))
print("Floor x // y = {}".format(x//y))
print("Modulo x % y ={} \n".format(x % y))

#28. Python Assignment Operators

print("assign variable x with 8, use x = 8")
a = 8
print("x is {}".format(a))

print("assign with addition, a += 3 we will get result 11 cause a += 3 is a = a + 3")
a+=3
print("a is {}".format(a))

print("assign with subtraction, a -= 2 we will get result 9 cause a -= 2 is a = a - 2")
a-=2
print("a is {}".format(a))

print("assign with multiplication, a *= 2 we will get result 18 cause a *= 2 is a = a * 2")
a*=2
print("a is {}".format(a))

print("assign with division, a /= 3 we will get result 6 cause a /= 3 is a = a / 3")
a/=2
print("a is {}".format(a))

print("assign with floor, a //= 4 we will get result 4 cause a //= 4 is a = a // 4")
a//=2
print("a is {}".format(a))

print("assign with modulo, a %= 3 we will get result 1 cause a %= 4 is a = a % 4")
a%=3
print("a is {} \n".format(a))

#29. Python Comparison Operators

print("Equal Comparison, = ")
print("5 = 7 is {}".format(5 == 7))
print("8 = 8 is {}".format(8 == 8))
print("aku = kamu is {} \n".format('aku' == 'kamu'))

print("Not Equal Comparison, != ")
print("5 != 7 is {}".format(5 != 7))
print("8 != 8 is {}".format(8 != 8))
print("aku != kamu is {} \n".format('aku' != 'kamu'))

print("Less than Comparison, < ")
print("5 < 7 is {}".format(5 < 7))
print("8 < 8 is {}".format(8 < 8))
print("aku < aku is {}".format('aku' < 'aku')) #dihitung total urutan huruf
print("aku < akv is {}".format('aku' < 'akv')) #dihitung total urutan huruf
print("aku < akt is {} \n".format('aku' < 'akt')) #dihitung total urutan huruf

print("Greater than Comparison, > ")
print("5 > 7 is {}".format(5 > 7))
print("8 > 8 is {}".format(8 > 8))
print("aku > aku is {}".format('aku' > 'aku')) #dihitung total urutan huruf
print("aku > akv is {}".format('aku' > 'akv')) #dihitung total urutan huruf
print("aku > akt is {} \n".format('aku' > 'akt')) #dihitung total urutan huruf

print("Less Equal than Comparison, <= ")
print("5 <= 7 is {}".format(5 <= 7))
print("8 <= 8 is {}".format(8 <= 8))
print("aku <= aku is {}".format('aku' <= 'aku')) #dihitung total urutan huruf
print("aku <= akv is {}".format('aku' <= 'akv')) #dihitung total urutan huruf
print("aku <= akt is {} \n".format('aku' <= 'akt')) #dihitung total urutan huruf

print("Greater Equal than Comparison, >= ")
print("5 >= 7 is {}".format(5 >= 7))
print("8 >= 8 is {}".format(8 >= 8))
print("aku >= aku is {}".format('aku' >= 'aku')) #dihitung total urutan huruf
print("aku >= akv is {}".format('aku' >= 'akv')) #dihitung total urutan huruf
print("aku >= akt is {} \n".format('aku' >= 'akt')) #dihitung total urutan huruf

#30. Python Logical Operators

print("And Logical")
print("True and True is {}".format(True and True))
print("True and False is {}".format(True and False))
print("False and True is {} \n".format(False and True))
print("False and False is {} \n".format(False and False))

print("9 > 7 and 4 < 10 {}".format(9 > 7 and 4 < 10))
print("9 > 7 and 4 > 10 {}".format(9 > 7 and 4 > 10))
print("9 < 7 and 4 < 10 {} \n".format(9 < 7 and 4 < 10))
print("9 < 7 and 4 > 10 {} \n".format(9 < 7 and 4 > 10))

print("OR Logical")
print("True or True is {}".format(True or True))
print("True or False is {}".format(True or False))
print("False or True is {} \n".format(False or True))
print("False or False is {} \n".format(False or False))

print("9 > 7 or 4 < 10 {}".format(9 > 7 or 4 < 10))
print("9 > 7 or 4 > 10 {}".format(9 > 7 or 4 > 10))
print("9 < 7 or 4 < 10 {}".format(9 < 7 or 4 < 10))
print("9 < 7 or 4 > 10 {} \n".format(9 < 7 or 4 > 10))

print("NOT Logical")
print("not True is ") 
print(not(4 == 4 and 5 == 5 ))
print("not False is")
print(not(4 != 4 and 5 != 5 ))

