import unittest
from io import StringIO
from robot import *
from unittest.mock import patch

@patch("sys.stdout", StringIO())
class TestSuperAlgos(unittest.TestCase):
    
    @patch("sys.stdin", StringIO("Hal\n"))
    def test_name_input(self):
        output = "Hal"
        self.assertTrue(name_the_robot(), output)


    @patch("sys.stdin", StringIO("right\n"))
    def test_right_movement(self):
        output = 2
        name = "Hal"
        x = 10
        y = 10
        direction = 1
        self.assertEqual(direction_right(direction, name, x, y), output)
    

    @patch("sys.stdin", StringIO("left\n"))
    def test_left_movement(self):
        output = 0
        name = "Hal"
        x = 10
        y = 10
        direction = 1
        self.assertEqual(direction_left(direction, name, x, y), output)
    

    def test_forward_movement(self):
        output = "forward"
        input_from_user = "forward 10"
        name = "Hal"
        direction = 1
        x = 10
        y = 10
        self.assertEqual(moving_forward(input_from_user, name, direction, x, y)[3], output)


    def test_back_command(self):
        output = "back"
        input_from_user = "back 10"
        name = "Hal"
        direction = 1
        x = 10
        y = 10
        self.assertEqual(moving_backward(input_from_user, name, direction, x, y)[3], output)
    

    @patch("sys.stdin", StringIO("Hal\nsprint 5\noff\n"))
    def test_sprint(self):
        output = "sprint 1"
        input_from_user = "sprint 5"
        x = 0
        y = 0
        name = "Hal"
        direction = 1
        steps = 5
        self.assertEqual(keep_track_of_sprint(input_from_user, x, y, name, direction, steps)[2], output)
    
if __name__ == '__main__':
    unittest.main()