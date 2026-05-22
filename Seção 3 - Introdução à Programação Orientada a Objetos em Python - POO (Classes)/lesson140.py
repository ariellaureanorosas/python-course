# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (não tem self e nem cls)


class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
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


c1 = Connection.create_with_auth("Ariel", 1234)
c1.set_user("Ariel")

print(c1.user)
print(c1.password)
print(c1.soma(5, 7))
