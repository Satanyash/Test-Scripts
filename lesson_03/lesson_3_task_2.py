from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Xiaomi", "15T", "+79005553535"))
catalog.append(Smartphone("Apple", "11 Pro", "+79005553030"))
catalog.append(Smartphone("Samsung", "Galaxy S5", "+79005552020"))
catalog.append(Smartphone("Tecno", "Ultra 3", "+79005551515"))
catalog.append(Smartphone("Pixel", "Super 5", "+79005551010"))
n = len(catalog)
for i in range(0, n):
    catalog[i].getBrand()
    catalog[i].getModel()
    catalog[i].getPhoneNumber()
