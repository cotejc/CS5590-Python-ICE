import math
print("This is the  Reverse of a number.")
num = int(input("Enter number."))
reve = 0
while (num > 0):
    remain = num % 10
    rev = (rev * 10) + remain
    num = num // 10
print ("Reverse of entered number is = %d" %rev)

print("This is the Area and Circumferense.")
num = int(input("Enter the radius."))
area = math.pi * num * num
cir = 2 * math.pi * num

print ("The area is %d" %area, "and the circumference is %d" %cir)
