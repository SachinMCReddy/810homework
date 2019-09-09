'''Python Program to perform string and mathematical operation (Sachin MC Reddy) '''


import unittest
import random


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if (self.denominator < 0):   #correct if numerator 1 number and denominator of other number negative
            self.denominator = (self.denominator * -1) 
            self.numerator = (self.numerator *-1)
        if self.denominator == 0 :   #check if it being divided by zero
            raise ZeroDivisionError ("cant divide by zero")

    def simplify(self):
        a = self.numerator
        b = self.denominator
        r = 1
        while r != 0:
            r = a % b
            a, b = b, r
        self.numerator /= a
        self.denominator /= a
        print(self.numerator, "/" , self.denominator)
        



def count_vowel(s1):
    ss1 = s1.lower()
    num = 0
    for char in ss1:
        if char in "aeiou":
            num=num+1
    print("There are", num, "Vowels in the sentence")
    return num

def list_travel(ele, list):
    print("list is", list)
    count = len(list)
    for i in list[::-1]:
        count = count-1
        if i == ele:
            print(ele,"latest list index is ", count)
            return count
    return None

def my_enumerate(seq):
    i=0
    for item in seq:
        print(i, item)
        i=i+1
        


def find_target(target, min_value, max_value, max_attempts):
    a=1
    while max_attempts >= a:
        
        r = random.randint(min_value, max_value)
        if(target == r):
            print("Guessed",r,"Target reached in ", a, "Tries" )
            break
        elif (target != r):
            print("Number guessed is", r,"Trying again" )
            a=a+1
            continue
    else:
        print("target couldnt be reached in",a-1,"attempts try again" )




class Tests(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowel('helloworld'), 3)
        self.assertEqual(count_vowel('hEllO wrld'), 2)
        self.assertEqual(count_vowel('hll wrld'), 0)

    def test_list_travel(self):
        ele='abc'
        l=['a','ab','abc','abcd','e']
        self.assertEqual(list_travel(ele,l), 2)
        self.assertEqual(list_travel('e',l), 4)   
        self.assertEqual(list_travel('apple', ['orange', 'apple', 'banana','apple','jackfruit','grapes','apple']), 6)     
       
    def test_fraction_simplify(self):
  
        (Fraction(4,-2)).simplify() == Fraction(-2,1)
    
    
    
def main():
    #Part 1 input vowels 
    print("Part 1 vowel search")
    s1=input("Enter your string ")
    count_vowel(s1)

    #Part 2 input for element to be searched
    print("Part 2 list travel")
    ele= input("Enter the element you want to be searched: ")
    list=input("Enter the list with a comma between elements: ")
    list = list.split(",")
    list_travel(ele ,list)

    #Part 3 input for num and den 
    print("Part 3 fraction simplification")
    nr= int(input("Enter numerator"))
    dn= int(input("Enter denominator"))
    Fraction(nr,dn).simplify()       

    #Part 4 input string 
    print("Part4 string enumerate")
    seq=input("Enter the input string :  ")
    my_enumerate(seq)

    #Part 5 input for min nad max
    print("Part 5 finding target value by generating random numbers")
    min_value=int(input("Enter the mininum value: "))
    max_value=int(input("Enter maximun value: "))
    target=int(input("Enter target: "))
    max_attempts=int(input("Enter max attempts: "))
    if min_value > max_value:
        raise ValueError("Min value cannot be greater than max value")
    if (target > max_value) and (target < min_value):
        raise ValueError("Target cannot be above max value")

    find_target(target, min_value, max_value, max_attempts)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
