class Mailing:
    def __init__(self, _to_address, _from_address, _cost, _track):
        self.to_address = _to_address
        self.from_address = _from_address
        self.cost = _cost
        self.track = _track

    def __str__(self):
        return (f"Отправление {self.track} из {self.to_address} в "
                f"{self.from_address}. Стоимость {self.cost} рублей")
