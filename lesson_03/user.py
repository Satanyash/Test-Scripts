class User:

    def __init__(self, _name, _last_name):
        self.name = _name
        self.last_name = _last_name

    def getName(self):
        print("Имя пользователя:", self.name)

    def getLastName(self):
        print("Фамилия пользователя:", self.last_name)

    def getFullName(self):
        print("Полное имя пользователя:", self.name, self.last_name)
