class Smartphone:

    def __init__(self, _brand, _model, _phone_number):
        self.brand = _brand
        self.model = _model
        self.phone_number = _phone_number

    def getBrand(self):
        print(self.brand, end=" - ")

    def getModel(self):
        print(self.model, end=". ")

    def getPhoneNumber(self):
        print(self.phone_number)
