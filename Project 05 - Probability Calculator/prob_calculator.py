import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls:
            ball_col = key
            ball_num = value
            for i in range(0, ball_num):
                self.contents.append(ball_col)
    
    def draw(self, num_to_draw):
        # use pop() or remove() together with random lib to pull out random items (modifying main self.contents list for ongoing prbability calculations)

#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
