'''
from py_expression_eval import Parser
parser = Parser()

expr = 'sqrt(x**2)'
vars = parser.parse(expr).variables()

print(parser.parse(expr).simplify({}).toString())
'''

import cmath

#TODO add precision, number of digits and so on
def prettifyNumber(num, eps=1e-12):
    re = num.real
    im = num.imag

    outValue = "{:.20f}".format(re)
    if abs(im)>eps:
        outValue += " + {:.20f}i".format(im)
    
    return outValue

#only works for non symbolic values
#TODO we need 2 roots every time
# we doesn't need send "SOMETHING WENT WRONG" every time, it's bad

def getSqrt(expr):
    #cmath's complex numbers need's to have j as an imaginary unit
    expr = expr.replace("i","j")
    
    try:
        result = eval(f'cmath.sqrt({expr})')
        return prettifyNumber(result)
    except:
        return "Something went wrong"

