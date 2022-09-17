# problems = '1234 + 56'
#from re import A



# problems = ['3801 - 2', '123 + 49']
# problems = ['1 + 2', '1 - 9380']
# problems = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
# problems = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
# problems = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']
# problems = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
# problems = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
# problems = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
# problems = [['3 + 855', '988 + 40'], True]
problems = [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True]


# check if optional argument has been provided & assume default to not provide calculated answer
give_calc = False
if (len(problems) > 1) and problems[1] == True:
    prob_list = problems[0]
    give_calc = True
else:
    prob_list = problems


# check for max number of problems
if len(prob_list) > 5:
    arranged_problems = "Error: Too many problems."
else:
    # break down input problems into component parts, then find row width & calculation
    sublists = []
    
    for n in prob_list:
        prob_parts = n.split()
        

        # determine row width & store as second to last value in prob_parts list
        max_len = 0
        for part in prob_parts:
            if len(part) > max_len:
                max_len = len(part)
        
        if max_len > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            break
        
        row_width = max_len + 2 # add 2 spaces to account for operator and one space afterward
        prob_parts.append(row_width)

        
        # calculate answer & store as last value in prob_parts list
        operand_a = prob_parts[0]
        operator = prob_parts[1]
        operand_b = prob_parts[2]


        if (operand_a.isdigit() == False) or (operand_b.isdigit() == False):
            arranged_problems = "Error: Numbers must only contain digits."
            break
        elif operator not in ['+', '-']:
            arranged_problems = "Error: Operator must be '+' or '-'."
            break
        elif operator == '+':
            answer = str(int(operand_a) + int(operand_b))
        elif operator == '-':
            answer = str(int(operand_a) - int(operand_b))
        else:
            arranged_problems = "Weird error - not sure what..."
        prob_parts.append(answer)


        sublists.append(prob_parts)


        # set up empty strings to concatenate each overall row for printing final output
        top_row = ''
        bottom_row = ''
        dash_row = ''
        calc_row = ''

        # loop through each problem within sublists to vertically reformat with spaces and include in overall rows for printing
        for n in sublists:
            top_operand = n[0]
            bot_operator = n[1]
            bot_operand = n[2]
            width = n[3]
            calc_answer = n[4]

            top = (' ' * (width - len(top_operand))) + top_operand
            bottom = bot_operator + (' ' * (width - 1 - len(bot_operand))) + bot_operand
            dash = '-' * width
            calc = (' ' * (width - len(calc_answer))) + calc_answer

            if n != sublists[-1]:
                top += ' ' * 4
                bottom += ' ' * 4
                dash += ' ' * 4
                calc += ' ' * 4
            
            top_row += top
            bottom_row += bottom
            dash_row += dash
            calc_row += calc


        if give_calc == True:
            arranged_problems = top_row + '\n' + bottom_row + '\n' + dash_row + '\n' + calc_row
        else:
            arranged_problems = top_row + '\n' + bottom_row + '\n' + dash_row


print(arranged_problems)