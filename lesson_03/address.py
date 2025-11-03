class Address:
    def __init__(self, _index, _city, _street, _house, _apartment):
        self.index = _index
        self.city = _city
        self.street = _street
        self.house = _house
        self.apartment = _apartment

    def __str__(self):
        return (f"{self.index}, {self.city}, {self.street}, "
                f"{self.house} - {self.apartment}")
