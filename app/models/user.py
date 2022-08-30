class User(object):
    def __init__(self, id , password) :
        self.id = id
        self.password = password
    
    def input_id(self) :
        return self.id
    
    def input_password(self) :
        return self.password