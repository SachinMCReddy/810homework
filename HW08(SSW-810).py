""" Pyhton program for Date arithmetic """
import datetime
import os
import unittest
from prettytable import PrettyTable
from datetime import timedelta

def date_arth():
    d1 = "Feb 27 2000"
    d2 = "Feb 27 2017"
    d3 = "JAN 1 2017"
    d4 = "OCT 31 2017" 
    dt1 = datetime.datetime.strptime(d1, '%b %d %Y')
    dt2 = datetime.datetime.strptime(d2, '%b %d %Y')
    dt3 = datetime.datetime.strptime(d3, '%b %d %Y')
    dt4 = datetime.datetime.strptime(d4, '%b %d %Y')
    dt3_str = dt3.strftime('%m/%d/%Y')
    dt4_str = dt4.strftime('%m/%d/%Y')


    end_date = dt1 + datetime.timedelta(days = 3)
    print('{} is the date after {}'.format(end_date, dt1))
    end = dt2 + datetime.timedelta(days = 3)
    print('{} is the date after {}'.format(end, dt2))
    delta = dt4 - dt3
    print('{} days passed between {} and {} '.format(delta.days, dt3_str, dt4_str))


def field_sep(path, num_fields, seperator=',', header=False):
    a = open(path, 'r')
    with a:
        for i, line in enumerate(a):
            line_split = line.rstrip("\n")
            line_split = line_split.split(seperator)
            if len(line_split) != num_fields:
                raise ValueError(f"{path} line: {i+1}: read {len(line_split)} fields but expected {num_fields}")
            if header and i == 0 :
                continue
            yield tuple(line_split)



def create_prettyT(input1):
    #Create table by using input from the prettytable
    dt = pretty_table(input1)
    pt = PrettyTable(field_names=['File Name', 'Number of Classes',
                                  'Number of Functions', 'Number of Lines', 'Number of Characters'])

    if len(dt) > 0:
        for a, classes, function, lines, character in dt:
            pt.add_row([a, classes, function, lines, character])
        print(pt)
            


def pretty_table(input1):
    #returns the number of characters, functions, classes
    try:

        character = 0
        classes = 0
        function = 0
        lines = 0
        summary = []

        print("\nCount of file ", input1)
        
        for f in os.listdir(input1):
            if f.endswith('.py'):
                a = os.path.join(input1, f)
                fp = open(a, 'r')
                with fp:
                    for line in fp:
                        character += len(line)
                        lines += 1
                        line = (line.strip())
                        if line.startswith('def '):
                            function += 1
                        if line.startswith('class '):
                            classes += 1

                summary.append((a, classes, function, lines, character))
                
            
        return summary
    except FileNotFoundError:
        print("Cant open directory:", input)


    
class Test(unittest.TestCase):
    #Unittest cases 
    def test_pretty_table(self):
        p1 = '/Users/SachinmcReddy/Desp/810-test'
        e1 = [('/Users/SachinmcReddy/Desktop/810-test/0_defs_in_this_file.py', 0, 0, 3, 57), ('/Users/SachinmcReddy/Documents/810-test/HW01-Sachin-2.py', 0, 2, 87, 1948)]
        self.assertEqual(pretty_table(p1), e1)

        self.assertEqual(pretty_table('No_directory_found'), None)
       
       
    
    def test_field_sep(self):
        path = "/Users/Sachinmc/Desktop/python/HW08.csv"
      
        expected = [('CarrierName', 'Phone', 'Year', 'Total Users ', 'Data usage '),
         ('Verizon', 'Iphone6s', '2018', '9249.03', '57.267'), 
         ('AT&T', 'Iphone7s', '2018', '4490.93', '636.93'), 
         ('Airtel', 'Iphone1', '2018', '6401.03', '364.50'), 
         ('T-mobile', 'Iphone4', '2018', '2475.30', '763.47'),
          ('spirit', 'Iphone5', '2018', '4929.02', '574.91'), 
          ('lyca', 'Iphone5s', '2018', '3965.20', '862.09'), 
          ('verizon canada', 'Iphone7', '2018', '8903.02', '673.37'), 
          ('AT&T canada', 'Iphone7s', '2018', '3173.02', '938.06'), 
          ('Airtel canada', 'Iphone8', '2018', '4984.02', '561.21'),
           ('T-Mobile canada', 'Iphone8S', '2018', '5450.02', '417.84'), 
           ('spirit canada', 'IphoneX', '2018', '9118.02', '912.23'), 
           ('lyca canada', 'IphoneXs', '2018', '9750.02', '762.68'), 
           ('Verizon: CDD', 'NOC', '2018', '1748.0', '856.10'), ('AT&T: CDD', 'OEC', '2018', '0759.0', '564.285 '), ('Airtel', 'LCN', '2018', '224.022', '749.284'), ('Tmobile', 'LAC', '2018', '238.033', '244.863'), ('spirit', '2018', '814.220','339.616'), ('lyca', 'DDS', '2018', '357.330', '421.272')]
        self.assertEqual(list(field_sep(path, 5)), expected)

        with self.assertRaises(ValueError) as context:
            list(field_sep(path, 6))

        self.assertEqual(str(context.exception), f"{path} line: 1: read 5 fields but expected 6")


def main():
    date_arth()
    unittest.main(exit=False, verbosity=2)

            
 

if __name__ == '__main__':
    main()


