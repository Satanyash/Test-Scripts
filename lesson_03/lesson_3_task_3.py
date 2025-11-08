from address import Address
from mailing import Mailing

to_address = Address(145955, "Москва", "Красная", 15, 143)
from_address = Address(675866, "Сочи", "Нижняя", 5, 14)
mail = Mailing(to_address, from_address, 213, "18JF43FF32")

print(mail)
