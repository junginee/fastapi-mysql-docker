from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) -> None:
        pass
        
    def calculate(self, first, second):
        calculator = Calculator(first, second)
        print(f'첫번째수: {calculator.first}')
        print(f'두번째수: {calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.subtract()}')
        print(f'{calculator.first} * {calculator.second} = {calculator.multi()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.divide()}')
        