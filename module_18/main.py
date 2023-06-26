num_tickets = int(input("Сколько билетов вы хотите купить: "))
price = 0

for i in range(1, num_tickets + 1):
    age = int(input(f"\nВведите возраст для билета {i}: "))
    if age < 18:
        print("Билет бесплатный")
    elif 18 <= age < 25:
        price += 990
        print("Стоимость билета 990 руб.")
    else:
        price += 1390
        print("Стоимость билета 1390 руб.")
    i += 1

if num_tickets > 3:
    price *= 0.9
    print("\nОбщая стоимость со скидкой 10%", price)
else:
    print("\nОбщая стоимость", price)
