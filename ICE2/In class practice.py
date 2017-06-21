#Jeremiah Cote - Student #1
#In Class Practice
#6/16/2017

sum = 0.0
count = 0
with open("test.txt") as f:
    for line in f:
        sum = sum + eval(line)
        count = count + 1
print("\nThe average of the numbers is", sum/count)