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
    
    def draw(self, num_to_draw):
        if num_to_draw > len(self.contents):
            drawn_balls = self.contents
            return drawn_balls
        else:            
            drawn_balls = random.choices(self.contents, k=num_to_draw)
            for n in drawn_balls:
                self.contents.pop(drawn_balls.index(n))
                        
            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # create deep copy of hat to draw from?
    
    num_outcome_matches = 0
    for i in range(0, num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        outcome = {}
        for n in drawn_balls:
            if n in outcome:
                outcome[n] += 1
            else:
                outcome[n] = 1
        # if outcome == expected_balls:
        #     num_outcome_matches += 1

        for color in expected_balls:
            if (color in outcome) and (outcome[color] >= expected_balls[color]):
                num_outcome_matches += 1

    probability = num_outcome_matches / num_experiments

    return probability
