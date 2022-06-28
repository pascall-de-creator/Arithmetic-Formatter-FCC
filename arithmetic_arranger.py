
def exception_handling(number1, number2, operator):
    '''
    Handle exceptions
    '''
    # invalid operator !( + or - )
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    # NaN
    try:
        int(number1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."
    # problem too long
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    return ""


def arithmetic_arranger(problems, displayMode = False):

    start = True
    side_space = "    "
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # Too many Problem exception handler
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    for problem in problems:
        separated_problem = problem.split()
        number1 = separated_problem[0]
        operator = separated_problem[1]
        number2 = separated_problem[2]
        exp = exception_handling(number1, number2, operator)

        if exp != "":
            return exp
        num1 = int(number1)
        num2 = int(number2)
        
        space = max(len(number1), len(number2))
        
        if start == True:
            line1 += number1.rjust(space + 2)
            line2 += operator + ' ' + number2.rjust(space)
            line3 += '-' * (space + 2)
            if displayMode == True:
                if operator == '+':
                    line4 += str(num1 + num2).rjust(space + 2)
                else:
                    line4 += str(num1 - num2).rjust(space + 2)
            start = False
        else:
            line1 += number1.rjust(space + 6)
            line2 += operator.rjust(5) + ' ' + number2.rjust(space)
            line3 += side_space + '-' * (space + 2)
            if displayMode == True:
                if operator == '+':
                    line4 += side_space + str(num1 + num2).rjust(space + 2)
                else:
                    line4 += side_space + str(num1 - num2).rjust(space + 2)
    # displayMode
    if displayMode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3