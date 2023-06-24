import numbers

import sympy as sym
from sympy import Function, log

from test_project.Exceptions.exceptions import NoParamExceprion
from test_project.helpers.converters import Converter


class log10(Function):
    @classmethod
    def eval(cls, x):
        return log(x) / log(10)


def calculate(expression, variables):
    if 'lg' in expression:
        expression = Converter.convert_log10(expression)

    expr = sym.simplify(expression)
    result = expr.subs(variables).replace(log, log10).evalf()
    number_of_symbols = len(result.free_symbols)

    if number_of_symbols >= 1:
        raise NoParamExceprion(number_of_symbols, result.free_symbols)

    if not isinstance(result, numbers.Number):
        try:
            eval(expression, variables)
        except ZeroDivisionError:
            raise ZeroDivisionError

    return Converter.convert_to_serializable_type(result)

# log(10+log(10))*5+lg(100) = 7,2069634257911252037509998562151
