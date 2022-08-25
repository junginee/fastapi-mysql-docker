from app.models.user import User

class UserService(object) :
    def __init__(self) -> None:
        pass
    
    def login(self, id , password) :
        user = User(id , password)
        print(f'id : {user.id}')
        print(f'password : {user.password}')