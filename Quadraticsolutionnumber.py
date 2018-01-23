import math
def b_plus(a, b, c):
    if b > 0:
        x = ((b - (2 * b)) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    elif b == 0:
        x = (0 + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    else:
        x = ((b - (2 * b)) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        
    return x
        
def b_minus(a, b, c):
    if b > 0:
        x = ((b - (2 * b)) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    elif b == 0:
        x = (0 - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    else:
        x = ((b - (2 * b)) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)

    return x

count = 0

print ("Quadratic Equations: ax^2+bx+c = 0")
#Ask user for A,b,and c values
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
#using the equation of(b^2-4ac) to determine the amount of solutions that any given equation can have.
if ((b * b)- 4 * a * c) > 0:
    count = 2
elif ((b * b)- 4 * a * c) == 0:
    count = 1
else:
    count = 0
#giving the variable count a value basing on the results from ((b * b)- 4 * a * c) 
if count == 0:
    print("Equaltion: " + str(a) + "x^2+" + str(b) + "x+" + str(c) + "=0 has " + "no" + " solutions.")
elif count == 1:
    solution1 = b_minus(a, b, c) #using the defined formulas to calculate the possible value of 
    print("Equaltion: " + str(a) + "x^2+" + str(b) + "x+" + str(c) + "=0 has " + "one" + " solutions.")
    print("Solution:" + str(int(solution1)))
elif count == 2:
    solution1 = b_minus(a, b, c) #the two possible solutions when the equation have two solutions
    solution2 = b_plus(a, b, c)
    print("Equaltion: " + str(a) + "x^2+" + str(b) + "x+" + str(c) + "=0 has " + "two" + " solutions.")
    print("Solution1:" + str(solution1))
    print("Solution2:" + str(solution2))
#since when count ==0 there is no solutions so we print that there is not solutio
#and do the same thing for the when count=1 and when count =2

