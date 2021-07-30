import unittest, os
import Audio2Album as toalbum
from datetime import datetime

print('\hey', '\\hey', '\\\hey', '\\\\hey')

def asserter(self, tests, func):
    for test in tests:
            try:
                for i in test[0]:
                    print(f'Testing {func(i)} against {test[1]}')
                    self.assertEqual(func(i), test[1])
            except:
                print(f'Testing {func(test[0])} against {test[1]}')
                self.assertEqual(func(test[0]), test[1])

class TestAudio2Album(unittest.TestCase):

    def test_getTime(self):
        print("Testing getTime()")
        func = toalbum.getTime
        
        tests = [
            ('0', datetime(1900, 1, 1)),
            ('10', datetime(1900, 1, 1, 0, 0, 10)),
            (['01:0', '1:0', '1:00'], datetime(1900, 1, 1, 0, 1, 0)),
            (['01:00:00', '1:0:0', '01:00:0'], datetime(1900, 1, 1, 1, 0, 0))
            ]

        asserter(self, tests, func)

        self.assertEqual(func('end'), 'END')

    def test_toMilli(self):
        print("Testing toMilli()")
        func = toalbum.toMilli

        tests = [
            (datetime(1900, 1, 1, 0, 0, 10), 10*1000),
            (datetime(1900, 1, 1, 0, 1, 0), 60*1000),
            (datetime(1900, 1, 1, 1, 0, 0), 60*60*1000)
        ]

        asserter(self, tests, func)

    def test_getPath(self):
        print("Testing getPath()")
        func = toalbum.getPath

        tests = [
            (['.\hey', 'hey', '.\hey'], os.path.join(os.getcwd(), 'hey')),
            (['.\hello\hey', 'hello/hey'], os.path.join(os.getcwd(), 'hello\hey'))
        ]

        asserter(self, tests, func)
    
    def test_sliceMain(self):
        pass




if __name__ == '__main__':
    unittest.main()