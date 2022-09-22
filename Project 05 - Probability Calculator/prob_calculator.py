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
    
    num_outcome_matches = 0 # incremented up only when full match condition (for multiple colors) is met within an experiment attempt

    # draw balls from hat for correct number of experiments
    for i in range(0, num_experiments):
        hat_exp = copy.deepcopy(hat) # make copy to start fresh in each experiment attempt
        drawn_balls = hat_exp.draw(num_balls_drawn)
        
        # convert drawn ball outcome from list to dictionary, to compare against expected_balls argument
        outcome = {}
        for n in drawn_balls:
            if n in outcome:
                outcome[n] += 1
            else:
                outcome[n] = 1
        
        # for each expected color, check if experiment outcome includes at least as many balls as expected
        all_colors_match = [] # ensure that match is met for all colors within expected_balls
        
        for key, value in expected_balls.items():
            expected_col = key
            expected_num = value

            if (expected_col in outcome) and (outcome[expected_col] >= expected_num):
                all_colors_match.append(True)
            else:
                all_colors_match.append(False)
    
        # if all colors in expected_balls were matched, increment total num_outcome_matches
        if all(all_colors_match):
            num_outcome_matches += 1

    probability = num_outcome_matches / num_experiments

    return probability
