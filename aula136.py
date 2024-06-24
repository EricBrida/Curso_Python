# method vs @classmethod vs @staticmethod
# method -> self, método e instância
# @classmethod -> cls, método de classe
# @staticmethod -> método estático (X self, X cls)

class Conection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y


c1 = Conection.create_with_auth('Luiz', '1234')
# c1 = Conection()
# c1.set_user('Eric')
# c1.set_password('xyz')
print(c1.user)
print(c1.password)
print(Conection.soma(2,3))