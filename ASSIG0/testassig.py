from ass1 import vowelsremover 
from ass2 import findelem
from ass3 import numbers
from ass4 import calcarea  
from ass5 import dic
from bons import vowelsremover  
import unittest
class testass1(unittest.TestCase):
    def test_task_one(self):
        self.assertEqual(vowelsremover('mobile'),'mbl')

class testass2(unittest.TestCase):
    def test_task_one(self):
        self.assertEqual(findelem('This is javaScript','i'),[2, 5, 15])

class testass3(unittest.TestCase):
    def test_task_one(self):
        self.assertEqual(numbers(3),[[1],[2, 4],[3, 6, 9]])

class testass4(unittest.TestCase):
    def test_task_one(self):
        self.assertEqual(calcarea('t',5,6),15)
    
    def test_task_one(self):
        self.assertEqual(calcarea('r',5,6),30)

    def test_task_one(self):
        self.assertEqual(calcarea('r',5),25)

    def test_task_one(self):
        self.assertEqual(calcarea('c',5),78.5)

class testass5(unittest.TestCase):
    def test_task_one(self):
        self.assertEqual(dic(['ahmed','mohamed','fatma','ali']),{'m': ['mohamed'], 'f': ['fatma'], 'a': ['ahmed', 'ali']})

class testbons(unittest.TestCase):
    def test_task_one(self):
        self.assertEqual(vowelsremover(['sara','ali']),['sr', 'l'])

if __name__ == '__main__':
    unittest.main()