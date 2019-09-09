
from collections import Counter
from collections import defaultdict
import unittest

#Anagram lists
def anagram(x1, x2):  
    a1 = list(x1)
    a2 = list(x2)
    a1.sort()
    a2.sort()
    return a1 == a2

#Anagram counter
def cntr_anagram(x1, x2):  
    return Counter(x1) == Counter(x2)

#Anagram default dictionary
def dd_anagram(x1, x2):
    b = defaultdict(int)
    for char in x1:
        b[char] += 1
    for char in x2:
        b[char] -= 1
    for c in b:
        if b[c] != 0:
            return False
    return True


#Covers alphabet(a-z)
def covers_alplabet(sentence):  
    d = set()
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower()
    for e in sentence:
            if e == ' ':
                continue
            else:
                d.add(e)
    return d == alpha

#Book index Default Dictionary
def book_index(words):  
    idx = defaultdict(set)
    result1 = list()
    for word, page in words:
        idx[word].add(page)

    for word in sorted(idx.keys()):
        result1.append([word, sorted(idx[word])])

    return result1


class listmanupulation(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram("dusty", "study"), True)
        self.assertEqual(anagram("dusty", "studys"), False)

    def test_dd_anagram(self):
        self.assertEqual(dd_anagram("dusty", "study"), True)
        self.assertFalse(dd_anagram("dusty", "studys"))

    def test_cntr_anagram(self):
        self.assertTrue(cntr_anagram("dusty", "study"), True)

    def test_covers_alplabet(self):
        self.assertTrue(covers_alplabet(
            "Pack my box with five dozen liquor jugs"))
        self.assertFalse(covers_alplabet(
            "Pack my box with five dozen liquor jugs."))

    def test_book_index(self):
        words = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1),
                 ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        words2 = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]],
                  ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        self.assertEqual(book_index(words), words2)


def main():

    a1 = input("Check the anagram  \n  Enter first word: ")
    a2 = input("Enter second word: ")

    print(anagram(a1, a2))
    print(dd_anagram(a1, a2))
    print(cntr_anagram(a1, a2))

    sentence = input("To check if sentence has all alphabets \n Enter input: ")
    print(covers_alplabet(sentence))

    words = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1),
             ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
    x = book_index(words)
    print(x)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()