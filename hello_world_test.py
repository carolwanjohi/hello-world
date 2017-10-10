import unittest
from hello_world import hello_world_function

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_function(self):
        '''
        Test if the hello world method returns "Hello, World"
        '''
        self.assertEqual(hello_world_function(), "Hello, World")

if __name__ == '__main__':
    unittest.main()
