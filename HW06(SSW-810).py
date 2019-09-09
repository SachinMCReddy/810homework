'''Python program to check function of pwd, insertion sort, remove vowels, BTree'''

import unittest



def check_pwd(pwd):
    # check_pwd function to check if pwd contain at least one upper & lower and ends with 1 digit
    v = [any(i.isupper() for i in pwd) and any(i.islower() for i in pwd) and pwd[-1].isdigit()]
    return v



def insertion_sort(sort):
    # Insertion sort function 
    sortf = []
    for i in sort:
        for offset, c in enumerate(sortf):
            if c >= i:
                sortf.insert(offset, i)
                break
        else:
            sortf.append(i)
    return sortf


def remove_vowelss(s):
    #Remove Vowels Function in List
    ns1 = []
    ns = list(s)
    [ns1.append(i) for i in ns if i not in "aeiouAEIOU"]
    return "".join(ns1)

class BTree(object):

    def __init__(self, value):
        #Create a new BTree 
        self.value = value 
        self.left = None
        self.right = None

    def find(self, value):
        #Return True is found or else false

        if self.value == value:
            return True

        elif self.value < value:
            if self.right:
                return self.right.find(value)
            else:
                return False

        elif self.value > value:
            if self.left:
                return self.left.find(value)
            else:
                return False

    def insert(self, value):
        #insert value as a new node in the appropriate spot 
        
        if self.value is None:
            self.value = value

        elif self.value == value:
            return
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BTree(value)
                else:
                    self.left.insert(value)

            elif value > self.value:
                if self.right is None:
                    self.right = BTree(value)
                else:
                    self.right.insert(value)

    def traverse(self):
        new_list=[]
        if self.left is not None:
            new_list = self.left.traverse()
        new_list.append(self.value)
        if self.right is not None:
            new_list.extend (self.right.traverse())
        return new_list



class test(unittest.TestCase):

    

    def test_check_pwd(self):
        str1 = "Hello1"
        str2 = "sachin"
        self.assertEqual(check_pwd(str1), [True])
        self.assertEqual(check_pwd(str2), [False])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([1, 5, 3, 3]), [1, 3, 3, 5])
        self.assertEqual(insertion_sort([1, 5, 3, 3, 3, 5]), [1, 3, 3, 3, 5, 5])
    
    def test_remove_vowelss(self):
        self.assertEqual(remove_vowelss("hello"), "hll")
        self.assertEqual(remove_vowelss("hi the app is free on you"), "h th pp s fr n y")
 
class BTreee(unittest.TestCase):

    def test_init(self):

        root = BTree(32)
        self.assertEqual(root.value, 32)
        self.assertEqual(root.right, None)
        self.assertEqual(root.left, None)
    
    def test_find(self):

        bt = BTree(32)
        bt.insert(2)
        bt.insert(11)
        bt.insert(3)

        self.assertEqual(bt.find(1), True)
        self.assertEqual(bt.find(11), True)
        self.assertEqual(bt.find(0), False)
        self.assertEqual(bt.find(7), False)
    

    def test_traverse(self):
        bt = BTree(32)
        bt.insert(2)
        bt.insert(11)
        bt.insert(3)

        self.assertEqual(bt.traverse(), [2,3,11,32])
        if __name__ == '__main__':
            unittest.main(exit=False, verbosity=2)
