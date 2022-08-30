from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService
from app.services.quiz import Quiz
from app.services.ddarung import DDarungService
from app.services.titanic import TitanicService
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, GRADE, \
    QUIZ_1, QUIZ_2, QUIZ_3, QUIZ_4, DDARUNG, TITANIC
class Url:
    
    def router(self, menu):
        if menu == LOGIN:
            UserService().login(
                input('id'), 
                input('password'))
        elif menu == CALCULATOR:
            CalculatorService().calculate(
                int(input('첫번째 값 입력: ')), 
                int(input('두번째 값 입력: ')))
        elif menu == TITANIC:
            titanicService = TitanicService()
            titanicService.submit(
                path='data/titanic/',train='train.csv', test='test.csv')
        elif menu == GRADE:
            name = input('이름')
            korean = int(input('국어'))
            english = int(input('영어'))
            math = int(input('수학'))
            print(f'이름: {name} \
                학점: {GradeService().get_grade(name,korean, english, math)}')
        elif menu == DDARUNG: DDarungService().submit(
            path='data/ddarung/', train='train.csv', test='test.csv'
        )
        
        elif menu == QUIZ_1: Quiz().quiz_1()
        elif menu == QUIZ_2: Quiz().quiz_2()
        elif menu == QUIZ_3: Quiz().quiz_3()
        elif menu == QUIZ_4: Quiz().quiz_4()
            