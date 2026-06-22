from smartphone import Smartphone


catalog = []
catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234567891"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79345678912"))
catalog.append(Smartphone("Huawei", "P40", "+79456789123"))
catalog.append(Smartphone("OnePlus", "Nord", "+79567891234"))
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
