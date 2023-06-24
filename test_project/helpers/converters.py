import sympy as sym


class Converter:
    @staticmethod
    def convert_log10(expr):
        return expr.replace('lg', 'log')

    @staticmethod
    def convert_to_serializable_type(obj):
        if isinstance(obj, sym.core.numbers.Integer) or int(str(obj).split('.')[1]) == 0:
            return int(obj)
        elif isinstance(obj, sym.core.numbers.Float):
            return float(obj)
        else:
            return obj.__str__()
