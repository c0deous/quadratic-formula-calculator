# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Quadratic Equation Solver #
# (c) 2016 Jesse Wallace (c0deous) #
# jessewallace.net

import os, sys, math
from fractions import Fraction

verbose = True # Set to False to disable explanations

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(text, color):
    try:
        colorcode = getattr(bcolors, color)
        return colorcode + text + bcolors.ENDC
    except AttributeError:
        return text

def inputm(textct):
    try:
        return raw_input(textct)
    except NameError:
        return input(textct)

def vr(input):
    if verbose == True:
        print(colored(input, 'OKBLUE'))

def vr_g(input):
    if verbose == True:
        print(colored(input, 'OKGREEN'))

def vr_r(input):
    if verbose == True:
        print(colored(input, 'FAIL'))

def main():
    print(colored('Quadratic Equations Calculator Mk. I', 'HEADER'))
    print(colored('(c) Jesse Wallace (c0deous) 2016', 'HEADER'))
    print(colored('jessewallace.net', 'HEADER'))
    print(' ')
    print('Quadratic Formula: (-b±√b²-4ac)/2a')
    print('Sample Quadratic Equation: ax²+bx+c=0')
    print(' ')
    var_a = int(inputm('What is A? '))
    var_b = int(inputm('What is B? '))
    var_c = int(inputm('What is C? '))
    
    var_as = str(var_a)  #--
    var_bs = str(var_b)  # Convert to strings for verbose mode (and my sanity)
    var_cs = str(var_c)  #--

    # Solve #
    # -b+/-sqrt(b^2-4ac)/2a
    vr(' ')
    vr('Follow the steps below to solve: ')
    vr(' ')
    vr('(-' + var_bs + '±√' + var_bs + '²-4(' + var_as + ')(' + var_cs + '))/2(' + var_as + ') - Substitute') # vr() tells steps in solving equation 
    equation_1 = -var_b # -b outside sqrt
    equation_2 = var_b ** 2 #-b^2 part inside sqrt
    equation_2b = 2 * var_a # The /2a part at the end
    equation_3 = 4 * var_a * var_c # 4*a*c inside sqrt
    equation_4 = equation_2 - equation_3 # b^2-4ac inside sqrt
    if equation_4 < 0: # EXTREMELY derpy way to change a negative number to positive and keep positive numbers positive. Replace this soon. Pls.
        equation_4 = str(equation_4)
        equation_4 = equation_4.strip('-')
        equation_4c = int(equation_4)
        pls_switch = True
    else:
        equation_4c = equation_4
    equation_5 = math.sqrt(equation_4c) # square root
    try:
        if pls_switch == True:
            equation_5 = - equation_5
    except NameError:
        pass
    # Equation splits into + or -
    vr('(' + str(equation_1) + '±√' + str(equation_4) + ')/' + str(equation_2b) + ' - Simplify')
    vr(' ')
    vr('Answer is + and - (splits into two parts)')
    equation_6 = equation_1 + equation_5
    equation_6b = equation_6 / equation_2b
    answer_positive = equation_6b
    vr(' ')
    vr_g('(' + str(equation_1) + '+' + str(equation_5) + ')/' + str(equation_2b) + ' - Simplify Positive Equation and Solve')

    equation_7 = equation_1 - equation_5
    equation_7b = equation_7 / equation_2b
    answer_negative = equation_7b
    vr_r('(' + str(equation_1) + '-' + str(equation_5) + ')/' + str(equation_2b) + ' - Simplify Negative Equation and Solve')

    # Convert answer to fraction (typically what the textbooks want)
    answer_positive_frac = Fraction(answer_positive)
    answer_negative_frac = Fraction(answer_negative)
    # Round answers to nearest hundreth
    answer_positive_round = math.ceil(answer_positive * 100) / 100.0
    answer_negative_round = math.ceil(answer_negative * 100) / 100.0

    # RETURN TO USER LAND
    print(' ')
    print('Raw: x = ' + colored(str(answer_positive), 'OKGREEN') + ', ' + colored(str(answer_negative), 'FAIL'))
    print('Simplified Fraction: x = ' + colored(str(answer_positive_frac), 'OKGREEN') + ', ' + colored(str(answer_negative_frac), 'FAIL'))
    print('Rounded to Nearest Hundredth: x = ' + colored(str(answer_positive_round), 'OKGREEN') + ', ' + colored(str(answer_negative_round), 'FAIL'))
    
if __name__ == '__main__':
    main()
