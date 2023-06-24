class NoParamExceprion(Exception):
    def __init__(self, number_of_symbols, params):
        if number_of_symbols == 1:
            self.message = "Требуемая переменная {0} не определена".format(params)
        elif number_of_symbols > 1:
            self.message = "Требуемые переменные {0} не определены".format(params)
