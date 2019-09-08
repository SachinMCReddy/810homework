''' python program that includes class fractions , plus , minus, times,
    divide ,equal  to perform tasks on calculator'''

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator <=0 :
            raise ValueError("This is not possible to divide by zero ")

    def __str__(self): # display fraction
        return str(self.numerator) + "/" + str(self.denominator)

    def plus(self, a): # For addition 
        num = (self.numerator * a.denominator) + (self.denominator * a.numerator)
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))
    
    def minus(self, a): # For subtraction 
        num = (self.numerator * a.denominator) - (self.denominator * a.numerator)
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))

    def times(self, a): # For multiplication
        num = (self.numerator * a.denominator) 
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))

    def divide(self, a): # For division 
        num = (self.numerator * a.denominator) 
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))
    
    def equal(self, a): # For equal 
        if (self.numerator * a.denominator) == (self.denominator * a.numerator):
            return True
        else:
            return False
    


def get_number(prompt): #input passed 
    while True:
        inpt = input(prompt)
        try:
            return float(inpt)
        except ValueError:
            print("Error: Please try again")  
        
def test():   #test function to demonstrate few functions

    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f34 = Fraction(3, 4)
    f33 = Fraction(3, 3)
 
    print(f12, '+', f12, '=', f12.plus(f12), '[4/4]')
    print(f44, '-', f12, '=', f44.minus(f12), '[4/8]')
    print(f12, '*', f34, '=', f12.times(f34), '[4/8]')
    print(f34, '/', f12, '=', f34.divide(f12), '[6/8]')
    print(f33, '=', f33, f33.equal(f33), '[TRUE]')
    

def main():
    print("welcome to the fraction calculator")    
    nm1 = get_number("Fraction one numerator") 
    dn1 = get_number("Fraction one denominator")
    operation = ["+", "-", "*", "/", "="]
    opp = input("operation (+, -, *, /, =)")
    if opp not in operation:
        print("invalid operator")
        return
    nm2 = get_number("Fraction two numerator") 
    dn2 = get_number("Fraction two denominator")
    f1 = Fraction(nm1, dn1)
    f2 = Fraction(nm2, dn2)

   #checking if the user input is the same as functions in the list printed[+, -, *, /]
    if opp == "+":           
        print(f1, "+", f2, "=", f1.plus(f2))
    elif opp == "-":
        print(f1, "-", f2, "=", f1.minus(f2))
    elif opp == "*":
        print(f1, "*", f2, "=", f1.times(f2))
    elif opp == "/":
        print(f1, "/", f2, "=", f1.divide(f2))
    elif opp == "=":
        print(f1, "=", f2, f1.equal(f2))

if __name__ == "__main__":
    test()
    main()
   
        

    
        

   
        




