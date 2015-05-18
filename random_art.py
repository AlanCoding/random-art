import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def pr(x, y):
    '''Function exists to implement some value persistence
    over verticle lines, it makes progress in random jumps along
    the spectrum between -1 and 1'''
    pr.pr_val += 2 * (random.random() - .5) * 0.015 * pr.pr_sign
    if pr.pr_val < -1:
        pr.pr_val = -1
        pr.pr_sign = 1
    elif pr.pr_val > 1:
        pr.pr_sign = -1
        pr.pr_val = 1
    return pr.pr_val  # *math.cos(x*5)
pr.pr_val = 0
pr.pr_sign = 1


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    def intensity(x, y):
        '''Function used to vary intensity of all colors at same time'''
        return 1 + 0.1 * math.sin(10 * math.sqrt(x**2 + y**2 + pr(x, y)**2))

    def expr1(x, y):
        return x * y * pr(x, y) * intensity(x, y)

    def expr2(x, y):
        return math.sqrt(x**2 + y**2 + pr(x, y)**2) * intensity(x, y)

    def expr3(x, y):
        return x * pr(y, x) * intensity(x, y)

    a_list = [expr1, expr2, expr3]
    create_expression.rgb += 1
    if create_expression.rgb >= 3:
        create_expression.rgb = 0
    return a_list[create_expression.rgb]

create_expression.rgb = 2


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""

    return expr(x, y)
