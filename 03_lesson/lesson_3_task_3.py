from address import Address
from mailing import Mailing


from_addr = Address(
    index=123456,
    city="Москва",
    street="Тверская",
    house=10,
    apartment=5
)

to_addr = Address(
    index=654321,
    city="Санкт-Петербург",
    street="Невский проспект",
    house=25,
    apartment=12
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="RF123456789RU"
)

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
