##################
#class Fraction
##################
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        self.simplify()
    def __str__(self):
        b=self.numerator//self.denominator
        if self.numerator%self.denominator==0:
            return str(b)
        elif b>0:
            return str(b)+"+"+str(self.numerator%self.denominator)+"|"+str(self.denominator)
        return str(self.numerator)+"|"+str(self.denominator)
#Here I first test to see if it will create a whole number meaning the remainder would be 0. 
#If it does print out the whole number. Then I check it the fraction is bigger than one.
#If it is I return the whole number plus the fraction using intiger divsion aswell as the remainder of the numerator divided by 
# the denominator. Last case is if it is less than 1 and not a whole number it prints out the fraction like normal
    
    def add(frac1,frac2):
        if frac1.denominator==frac2.denominator:
            return Fraction(frac1.numerator+frac2.numerator,frac1.denominator)
        denominator=frac1.denominator*frac2.denominator
        numerator=(frac1.numerator*frac2.denominator)+(frac1.denominator*frac2.numerator)
        return Fraction(numerator,denominator)
#first I check if denominator's were the same. If they were then i just added up the numerators and returned a fraction object.
#If not I used the equation (a1*b2+a2*b1)/(b1*b2)
    
    def subtract(frac1,frac2):
        if frac1.denominator==frac2.denominator:
            return Fraction(frac1.numerator-frac2.numerator,frac1.denominator)
        denominator=frac1.denominator*frac2.denominator
        numerator=(frac1.numerator*frac2.denominator)-(frac1.denominator*frac2.numerator)
        return Fraction(numerator,denominator)
#first I check if denominator's were the same. If they were then I just subtracted the numerators and returned a fraction object.
#If not I used the equation (a1*b2-a2*b1)/(b1*b2)

    def times(frac1,frac2):
        denominator=frac1.denominator*frac2.denominator
        numerator=frac1.numerator*frac2.numerator
        return Fraction(numerator,denominator)
#Used the equation (a1*a2)/(b1*b2) to get the numerator and denominator
    def divide(frac1,frac2):
        denominator=frac1.denominator*frac2.numerator
        numerator=frac1.numerator*frac2.denominator
        return Fraction(numerator,denominator)
#Used the equation (a1*b2)/(b1*a2) to get the numerator and denominator

    def simplify(self):
        numfact=factors(abs(self.numerator))
        demfact=factors(abs(self.denominator))
        num=0
        for i in range(len(numfact)-1,-1,-1):
            if numfact[i] in demfact:
                num=numfact[i]
                demfact.remove(num)
                numfact.remove(num)
                self.numerator=self.numerator//num
                self.denominator=self.denominator//num
#Here I called the factors for the numerator and denominator. Checked to find similarities in the lists. Removed the similarty 
#and then I divided by the number that was similar. I made sure to go backwards on my for loop so even if I remove an element I
#dont skip over anything

    #to complete   

############################################
#Functions #################################
############################################


# Testing functions
def test_str():
    print("General use")
    print("2/3",Fraction(2,3))
    print("1/6",Fraction(1,6))
    print("Corner cases")
    print("0/4",Fraction(0,4))
    print("3/1",Fraction(3,1))
    print("3/3",Fraction(3,3))
    print("-4/4",Fraction(-4,4))
    print("Mixed forms")
    print("3/2",Fraction(3,2))
    print("7/3",Fraction(7,3))
    print("6/3",Fraction(6,3))

def test_add():
    print("\nTest for static method add")
    print("1|4+2|4","Result=3|4","\tYours=",Fraction.add(Fraction(1,4),Fraction(2,4)))
    print("1|5+2|3","Result=13|15","\tYours=",Fraction.add(Fraction(1,5),Fraction(2,3)))
    print("1|4+3|8","Result=20|32","\tYours=",Fraction.add(Fraction(1,4),Fraction(3,8)))
    print("1|5+6|7","Result=1+2|35","\tYours=",Fraction.add(Fraction(1,5),Fraction(6,7)))

def test_subtract():
    print("\nTest for static method subtract")
    print("3|5-1|5","Result=2|5","\tYours=",Fraction.subtract(Fraction(3,5),Fraction(1,5)))
    print("1|5-3|5","Result=-2|5","\tYours=",Fraction.subtract(Fraction(1,5),Fraction(3,5)))
    print("2|3-1|12","Result=21|36","\tYours=",Fraction.subtract(Fraction(2,3),Fraction(1,12)))
    print("1|5-1|5","Result=0","\tYours=",Fraction.subtract(Fraction(1,5),Fraction(1,5)))
    print("9|4-7|8","Result=1+12|32","\tYours=",Fraction.subtract(Fraction(9,4),Fraction(7,8)))

def test_times():
    print("\nTest for static method times")
    print("2|3*1|7","Result=2|21","\tYours=",Fraction.times(Fraction(2,3),Fraction(1,7)))
    print("2|3*6|7","Result=12|21","\tYours=",Fraction.times(Fraction(2,3),Fraction(6,7)))
    print("4|5*5|4","Result=1","\tYours=",Fraction.times(Fraction(4,5),Fraction(5,4)))
    print("3|2*6|7","Result=1+4|14","\tYours=",Fraction.times(Fraction(3,2),Fraction(6,7)))

def test_divide():
    print("\nTest for static method divide")
    print("6|7/5|3","Result=18|35","\tYours=",Fraction.divide(Fraction(6,7),Fraction(5,3)))
    print("2|3/7|6","Result=12|21","\tYours=",Fraction.divide(Fraction(2,3),Fraction(7,6)))
    print("3|4/1|4","Result=3","\tYours=",Fraction.divide(Fraction(3,4),Fraction(1,4)))
    print("3|2/7|6","Result=1+4|14","\tYours=",Fraction.divide(Fraction(3,2),Fraction(7,6)))


def test_simplify():   
    print("List Prime Factors")
    print("0=",factors(0))
    print("18=",factors(18))
    print("364=",factors(364))
    print("Simplified forms")
    print("5/35",Fraction(5,35))
    print("12/48",Fraction(12,48)) 
    print("12/8",Fraction(12,8))

    
# add more functions as required (test_fraction_app) and (factors)
def test_fraction_app():
    print("------Fraction app----------")
    while True:
        a=input("Enter your fraction operation using (+,-,*,/): ")
        if a =="":
            print("Goodbye!")
            break
        elif "+" in a:
            L=a.split("+")
            num1=L[0].split("|")
            num2=L[1].split("|")
            f1=Fraction(int(num1[0]),int(num1[1]))
            f2=Fraction(int(num2[0]),int(num2[1]))
            print(Fraction.add(f1,f2))
        elif "-" in a:
            L=a.split("-")
            num1=L[0].split("|")
            num2=L[1].split("|")
            f1=Fraction(int(num1[0]),int(num1[1]))
            f2=Fraction(int(num2[0]),int(num2[1]))
            print(Fraction.subtract(f1,f2))
        elif "*" in a:
            L=a.split("*")
            num1=L[0].split("|")
            num2=L[1].split("|")
            f1=Fraction(int(num1[0]),int(num1[1]))
            f2=Fraction(int(num2[0]),int(num2[1]))
            print(Fraction.times(f1,f2))
        elif "/" in a:
            L=a.split("/")
            num1=L[0].split("|")
            num2=L[1].split("|")
            f1=Fraction(int(num1[0]),int(num1[1]))
            f2=Fraction(int(num2[0]),int(num2[1]))
            print(Fraction.divide(f1,f2))
#Here I did a while loop to keep repeating the program untill the exit(press enter).
#After I check to see which oporation they use, then split up the string twice to get the numbers and correctly place them into fraction
# objects. After I call the fuction that matches the operation 

def factors(num):
    if (num==0 or num==1):
        return []
    for i in range(2,num+1):
        if num%i==0:
           return ([i]+factors(num//i))
#Does a recursive funtion that calls itself and keeps returning the first prime factor it finds. In the end a list is returned of factors


########################################
#Main Program
########################################
# Uncoment all these incrementally for testing as you go along
# you can submit your project with everything commented here

#test_str()
#test_add()
#test_subtract()
#test_times()
#test_divide()
#test_fraction_app()
#test_simplify()
