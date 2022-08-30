from app.models.score import Score

class ScoreService(object) :
    def __init__(self) -> None:
        pass
    
    def info (self, name, score):
        info= Score(name, score)
        print(f'name : {info.name}')
        print(f'score : {info.score}')