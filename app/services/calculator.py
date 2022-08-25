from app.models.calculator import Calculator
class CalcuratorService(object): # 자식객체? 보호해야할 객체가 외부로 노출되는 것을 차단한다. 
     def __init__(self) -> None:
          pass
          
     def calculate(self, first, second):
          calculator = Calculator(first, second)
          print(f'첫번째수 : {calculator.first}')          # { 메모리영역 }
          print(f'두번째수 : {calculator.second}')   
          print(f' {calculator.first} + {calculator.second} = {calculator.sum()}')
          print(f' {calculator.first} - {calculator.second} = {calculator.subtract()}')
          print(f' {calculator.first} * {calculator.second} = {calculator.multiply()}')
          print(f' {calculator.first} / {calculator.second} = {calculator.divide()}')
          