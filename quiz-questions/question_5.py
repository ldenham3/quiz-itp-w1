"""Intro to Python - Week 1 - Quiz."""


# Question 5
def calculate_tax(income):
    """Implement the code required to make this function work.

    Write a function `calculate_tax` that receives a number (`income`) and
    calculates how much of Federal taxes is due,
    according to the following table:


    | Income  | Tax Percentage |
    | ------------- | ------------- |
    | <= $50,000    |        15%    |
    | <= $75,000    |        25%    |
    | <= $100,000   |        30%    |
    | > $100,000    |        35%    |

    Example:

    income = 30000  # $30,000 is less than $50,000
    calculate_tax(income)  # $30,000 * 0.15  = 4500 = $4,500

    income = 80000  # $80,000 is more than $75,000 but less than $80,000
    calculate_tax(income)  # $80,000 * 0.25 = 20000 = $20,000

    income = 210000  # $210,000 is more than $100,000
    calculate_tax(income)  # $210,000 * 0.35 = 73500 = $73,500
    """
    tax = 0
    if type(income) == int and income > 0:
        if income <= 50000:
            tax = income * 0.15
        elif income <= 75000:
            tax = income * 0.25
        elif income <= 100000:
            tax = income * 0.30
        else: 
            tax = income * 0.35
        return tax
    elif income == 0:
        return 0
    else:
        return "you did something invalid"
