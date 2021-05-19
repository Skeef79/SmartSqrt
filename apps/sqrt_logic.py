'''
from py_expression_eval import Parser
parser = Parser()

expr = 'sqrt(x**2)'
vars = parser.parse(expr).variables()

print(parser.parse(expr).simplify({}).toString())
'''

import cmath

#TODO add precision, number of digits and so on
def prettifyNumber(num, prec = 10):
    re = num.real
    im = num.imag
    eps = 1e-50

    #if imag <0 then add - 

    #if (abs(re)<eps and re<0):
     #   re = -re;


    reStr = '%.*f' % (prec, re)
    imStr = '%.*f' % (prec, im)

    #print(reStr)
    #print(imStr)


    outValue = reStr;
    if (abs(im)>eps):
        if im < 0:
            outValue+= f' - {imStr[1:]}i'
        else:
            outValue += f' + {imStr}i'

    return outValue

def convert(expr):
    result = "";
    expr = expr.replace("i","j")

    for i in range(len(expr)):
        cur = expr[i];
        if expr[i]=="j":
            if (i==0 or not expr[i-1].isdigit()):
                cur = "1"+cur
        result+=cur;

    return result;


def getSqrt(expr, prec = 10):
    #cmath's complex numbers need's to have j as an imaginary unit
    expr = convert(expr)

    print(expr)
    
    try:
        result = eval(f'cmath.sqrt({expr})')
        return prettifyNumber(num = result, prec = prec)
    except:
        return "Error"


def isfloat(root):
    try:
        float(root)
        return True
    except:
        return False

def getRoots(expr, prec = 50):
    root = getSqrt(expr, prec)
    if root == "Error":
        return "Error", "Error"
    
    root1 = root
    root2 = prettifyNumber(eval(convert(f'-({root})')), prec)
    return root1, root2

