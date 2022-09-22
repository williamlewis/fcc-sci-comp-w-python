import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            ball_col = key
            ball_num = value
            for i in range(0, ball_num):
                self.contents.append(ball_col)
        # self.original_contents = copy.deepcopy(self.contents)
    
    def draw(self, num_to_draw):
        if num_to_draw > len(self.contents):
            # self.contents = self.original_contents
            drawn_balls = self.contents
            return drawn_balls
        else:
            # indices_to_draw = []
            # for i in range(0, num_to_draw):
            #     indices_to_draw.append(random.randint(0, len(self.contents)))
            
            # drawn_balls = []
            # for i in indices_to_draw:
            #     drawn_balls.append(self.contents[i])
            #     self.contents.pop(i)
            
            drawn_balls = random.choices(self.contents, num_to_draw)
            # drawn_ball_indices = []
            # for n in drawn_balls:
            #     drawn_ball_indices.append(drawn_balls.index(n))
            for n in drawn_balls:
                self.contents.pop(drawn_balls.index(n))
                        
            return drawn_balls


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
