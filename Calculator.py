class Calculator:
    def addition(self,n1, n2):
        return n1 + n2

    def multiplication(self, n1, n2):
        return n1*n2

    def substraction(self, n1, n2):
        return n1-n2

    def division(self, n1, n2):
        try:
            result = n1 / n2
        except ZeroDivisionError:
            result = 0
        return result
