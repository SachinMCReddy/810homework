''' python program that includes class fractions , plus , minus, times,
    divide ,equal  to perform tasks on calculator'''
import unittest
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0 :
            raise ValueError("This is not possible to divide by zero ")

    def __str__(self): # display fraction
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, a): # For addition 
        num = (self.numerator * a.denominator) + (self.denominator * a.numerator)
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))
    
    def __sub__(self, a): # For subtraction 
        num = (self.numerator * a.denominator) - (self.denominator * a.numerator)
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))

    def __mul__(self, a): # For multiplication
        num = (self.numerator * a.denominator) 
        den = (self.denominator * a.denominator)
        return Fraction(float(num), float(den))

    def __truediv__(self, a): # For division 
        num = (self.numerator * a.denominator) 
        den = (self.denominator * a.denominator)
        return Fraction((num), (den))
    
    def __eq__(self, a): # For equal 
        if (self.numerator * a.denominator) == (self.denominator * a.numerator):
            return True
        else:
            return False
    
    def __ne__(self, a): # For not equal 
        if (self.numerator * a.denominator) != (self.denominator * a.numerator):
            return True
        else:
            return False
    
    def __lt__(self, a): # For less than 
        if (self.numerator * a.denominator) < (self.denominator * a.numerator):
            return True
        else:
            return False
    
    def __le__(self, a): # For less than or equal 
        if (self.numerator * a.denominator) <= (self.denominator * a.numerator):
            return True
        else:
            return False
    
    def __gt__(self, a): # For greater than  
        if (self.numerator * a.denominator) > (self.denominator * a.numerator):
            return True
        else:
            return False
    
    def __ge__(self, a): # For greater than equal 
        if (self.numerator * a.denominator) >= (self.denominator * a.numerator):
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
        
class FractionTest(unittest.TestCase): 
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)
        
    def test_str(self):
        """ verify that __str__() works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')
        
    def test_equal(self):
        """test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 == f3)
        self.assertFalse(f1 == Fraction(3, 5))

    def test_add(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(-1, 2)
        f5 = Fraction(2, -3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))
        self.assertTrue((f1 + f4) == Fraction(1, 4))
        self.assertTrue((f1 + f5) == Fraction(1, 12))
        self.assertTrue((f4 + f5) == Fraction(-7, 6))

    def test_sub(self):
        """test fraction subtract"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 5)
        f3 = Fraction(3, 8)
        f4 = Fraction(-1, 2)
        f5 = Fraction(2, -3)
        self.assertTrue((f1 - f3) == Fraction(1, 8))
        self.assertTrue((f1 - f2) == Fraction(1, 10))
        self.assertTrue((f2 - f3) == Fraction(1, 40))
        self.assertTrue((f1 - f4) == Fraction(2, 2))
        self.assertTrue((f1 - f5) == Fraction(7, 6))
        self.assertTrue((f4 - f5) == Fraction(1, 6))

    def test_mul(self):
        """test fraction multiple"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 5)
        f3 = Fraction(4, 7)
        f4 = Fraction(-1, 2)
        f5 = Fraction(2, -3)
        self.assertFalse((f1 * f2) == Fraction(6, 15))
        self.assertFalse((f1 * f3) == Fraction(8, 21))
        self.assertFalse((f2 * f3) == Fraction(12, 35))
        self.assertFalse((f1 * f4) == Fraction(-2, 6))
        self.assertFalse((f1 * f5) == Fraction(-4, 9))
        self.assertFalse((f4 * f5) == Fraction(2, 6))


    def test_truediv(self):
        """test fraction truedivide"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 5)
        f3 = Fraction(4, 7)
        f4 = Fraction(-1, 2)
        f5 = Fraction(2, -3)
        self.assertFalse((f1 / f2) == Fraction(5, 6))
        self.assertFalse((f1 / f3) == Fraction(7, 8))
        self.assertFalse((f2 / f3) == Fraction(21, 20))
        self.assertFalse((f1 / f4) == Fraction(2, -2))
        self.assertFalse((f1 / f5) == Fraction(-3, 4))
        self.assertFalse((f4 / f5) == Fraction(3, 4))

    def test_notequal(self):
        """test fraction notequal"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 5)
        f3 = Fraction(4, 7)
        self.assertTrue(f1 != f2)
        self.assertTrue(f1 != f3)
        self.assertTrue(f2 != f3)
        self.assertTrue(f1 != Fraction(1, 3))

    def test_lessthan(self):
        """test fraction less than"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 5)
        f3 = Fraction(5, 7)

        self.assertFalse(f2 < f1)
        self.assertTrue(f1 < f3)
        self.assertTrue(f2 < f3)


    def test_lessorequal(self):
        """test fraction less than or equal"""
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 5)
        f3 = Fraction(6, 7)

        self.assertTrue(f1 <= f2)
        self.assertTrue(f1 <= f3)
        self.assertTrue(f2 <= f3)
        self.assertTrue(f1 <= f1)
        self.assertTrue(f2 <= f2)


    def test_greaterthan(self):
        """test fraction greater than"""
        f1 = Fraction(5, 7)
        f2 = Fraction(3, 5)
        f3 = Fraction(1, 2)
        f4 = Fraction(-1, 2)
        f5 = Fraction(2, -3)
        self.assertTrue(f1 > f2)
        self.assertTrue(f1 > f3)
        self.assertTrue(f2 > f3)
        self.assertTrue(f5 > f4)
        self.assertTrue(f1 > f4)


    def test_greaterorequal(self):
        """test fraction greater than or equal"""
        f1 = Fraction(5, 7)
        f2 = Fraction(3, 5)
        f3 = Fraction(1, 3)

        self.assertTrue(f1 >= f2)
        self.assertTrue(f1 >= f3)
        self.assertTrue(f2 >= f3)
        self.assertTrue(f1 >= f1)

        
    


if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    
    unittest.main(exit = False, verbosity = 2)