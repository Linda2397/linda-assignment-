#Linda Ambassa
#Python Operators
#Assignment 1



#Assignment operators
#Bitwise Operators
print("Operators")
print("Arithmetic Operators")

#the + Operators Addition
x = input("Enter your first name: ")
y = input("Enter your last name:")

print("Hello! " + x + y)
#So this will sum x and y from the user input



# the * Operator
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

#printing value
print(a * b)

#the // operators

print("The // Operator")

c = input("Enter value of c: ")
d = input("Enter value of d: ")


print(c // d)


#the % Operator
print("The modulus Operator")

r = input("Value of r: ")
f = input("value of f: ")

print(r % f)

#the ** (Exponential) operator
print("The ** (Exponential) Operator")
i = input("Enter the value of i: ")
o = input("Enter the value of o: ")

print ( o ** i)



print("Comparison Operators")
print("The == operator")

l = input("Entter the value of l: ")
m = input("Enter the value of m: ")

print(l==m)

print("The != Operator")

q = input("Enter the value of q: ")
w = input("Enter the value of w: ")

print(q != w)

print("The > Operator")

t = input("Enter the value of t: ")
s = input("Enter the value of s: ")

if t > s:
    print("t is greater than s")

else:
    print("s is greater than t")

print("the < operator")

f = input("Enter the value of f: ")
h = input ("Enter the value of h: ") 

if f < h:
    print("f is smaller than h")

else:
    print("f is greater than h")

print("The >= operator")

u = input("Enter the value of u: ")
r = input("Enter the value of r: ")

if u >= r:
    print("r is smaller than u")

else:
    print("r is greater than u")

print("The <= operator")

q = input("Enter the value of q: ")
s = input("Enter the value of s: ")

if q <= s:
    print("q is smaller than s")

else:
    print("q is greater than s")

print("The Logical Operators")

print("Logical And")
x = input("Enter the value of x: ") 
y = input("Enter the value of y: ")

print(x < y and y < x)

print("Logical or")

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print(x < y or y < x)

print("Logical not")

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print(not(x < y and x > y))


print("Identity Operators")

print("Is Operator")

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print(x is y)

print("Is not operator")

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print(x is not y)

print("Membership Operator")
print("in operator")
#returns true if a sequence of values is found
x = ["Ambassa", "Angehi"]

print("Ambassa" in x)
print(x)

print("Not in operator")
#returns true if a sequence of values is found
x = ["Ambassa", "Angehi"]

print("Ambassa" not in x)
print(x)

print(2%6)

exit()
