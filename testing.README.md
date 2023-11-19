# breakout-game
import unittest: This imports the unittest module for writing and running tests.
from unittest.mock import patch: This imports the patch function from the unittest.mock module, which is used to replace parts of the code during testing.
import pygame: This imports the Pygame library for game development.

detect_collision Function:
instead of imporing the detect collision from the pygame, i wrote the code itself, This function takes the current ball position (ball). 


TestBlockBreakerGame Class:
This class inherits from unittest.TestCase, indicating that it contains test methods.

setUp Method: 
This method is called before each test case. It initializes the Pygame environment and sets up a display with a specified size.
tearDown Method: This method is called after each test case. It shuts down the Pygame environment.

Test Methods:
test_detect_collision: Tests the detect_collision function by checking if it returns a tuple and verifying its length.
test_ball_movement: Tests the movement of the ball after an update.
test_collision_with_paddle: Tests collision detection with a paddle, mocking the pygame.key.get_pressed function.

Main Execution:
if __name__ == '__main__': This condition checks whether the script is being run directly (not imported as a module), and if so, it runs the unittests using unittest.main().
Overall, this script provides a foundation for testing key functionalities of a Block Breaker game, focusing on the detect_collision function and the movement of the ball. It uses the Pygame library for game development and unittest for testing.

Reference 
https://www.youtube.com/watch?si=S12ryN5bv1VyYxj_&fbclid=IwAR3EglZae-QalhJKiVTTNoNgAC8r1--dlFEw5jJbwKqri_zDAtKsu1WZ4tU&v=v1MtwCPTmBI&feature=youtu.be
-The TestBlockBreakerGame class inherits from unittest.TestCase and contains test methods for the detect_collision function, ball movement, and collision with a paddle from my pygame called breakout.
-The script utilizes Pygame functions for creating a Pygame display, initializing Pygame, and working with Pygame Rect objects.


