from smartphone import Smartphone

catalog = [""] * 5
catalog[0] = Smartphone("Xiaomi", "15T", "+79005553535")
catalog[1] = Smartphone("Apple", "11 Pro", "+79005553030")
catalog[2] = Smartphone("Samsung", "Galaxy S5", "+79005552020")
catalog[3] = Smartphone("Tecno", "Ultra 3", "+79005551515")
catalog[4] = Smartphone("Pixel", "Super 5", "+79005551010")
n = len(catalog)
for i in range(0, n):
    catalog[i].getBrand()
    catalog[i].getModel()
    catalog[i].getPhoneNumber()
