"""Python program that  takes a string as an argument and returns a new string which is the reverse of the argument. """
import unittest

def reverse(s):
    #reverse function 
    rev = ""
    for i in s:
        rev = i + rev
    return rev

def rev_enumerate(sa):
    #reverse enumerator function 
    length = len(sa)
    for i in range(length-1, -1, -1):
        yield i, sa[i]

def find_second(target, ts):
    #second occurrence of target
    fs = ts.find(target)
    sc = ts.find(target, fs+1)
    if sc == -1:
        return -1
    else:
        return sc

def get_lines(path):
    # lines read and print without any commment 
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("can't open", path)
    else:
        with fp:
            sas = ""
            for line in fp:

                if line[len(line)-2].endswith("\\") is True:
                    sas = sas + line[:-2]
                    continue
                else:
                    sas = sas + line.strip()
                    hh = sas.find('#')
                    if hh == -1:
                        yield sas
                        sas = ""
                    elif hh == 0:
                        sas = ""
                        continue
                    else:
                        yield sas[:hh]
                        sas = ""

class GetLinesTest(unittest.TestCase):

    def test_reverse(self):
        #test the reverse case 
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("i am human"), "namuh ma i")
        self.assertEqual(reverse(""), "")

    def test_rev_enumerate(self):

        expect = [(4, 'o'), (3, 'l'), (2, 'l'), (1, 'e'), (0, 'h')]
        result = list(rev_enumerate("hello"))
        self.assertEqual(result, expect)

        expect = [(9, 'n'), (8, 'a'), (7, 'm'), (6, 'u'), (5, 'h'), (4, ' '),
                  (3, 'm'), (2, 'a'), (1, ' '), (0, 'i')]
        result = list(rev_enumerate("i am human"))
        self.assertEqual(result, expect)

    def test_find_second(self):

        self.assertEqual(find_second('iss', 'mississippi'), 4)
        self.assertEqual(find_second('mimi', 'hello mi mi mi mi'), -1)
        self.assertEqual(find_second('aba', 'ababa'), 2)

    def test_get_lines(self):
        #test lines using the file created with information
        file_name = '810.txt'

        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)