class User(object):
    def __init__(self, id, password) :
        self.id = id
        self.password = password
    
    def sum(self):
        return self.id + self.password   