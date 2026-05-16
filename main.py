from models import Car

cars = []


def add_car():
    print("\nДобавяне на автомобил")

    brand = input("Марка: ")
    model = input("Модел: ")

    try:
        year = int(input("Година: "))
        price = float(input("Цена: "))
    except ValueError:
        print("Невалидни данни!")
        return

    car = Car(brand, model, year, price)
    cars.append(car)

    print("Автомобилът е добавен успешно!")


def show_cars():
    print("\nВсички автомобили:")

    if not cars:
        print("Няма налични автомобили.")
        return

    for index, car in enumerate(cars, start=1):
        print(f"{index}. {car.show_info()}")


def search_by_brand():
    brand = input("\nВъведете марка за търсене: ")

    found = False

    for car in cars:
        if car.brand.lower() == brand.lower():
            print(car.show_info())
            found = True

    if not found:
        print("Няма намерени автомобили от тази марка.")


def sort_by_price():
    print("\nСортиране по цена:")

    sorted_cars = sorted(cars, key=lambda car: car.price)

    for car in sorted_cars:
        print(car.show_info())


def sell_car():
    show_cars()

    if not cars:
        return

    try:
        choice = int(input("\nИзберете номер на автомобил за продажба: "))

        if 1 <= choice <= len(cars):
            print(cars[choice - 1].sell_car())
        else:
            print("Невалиден номер.")

    except ValueError:
        print("Моля въведете число.")


def change_car_price():
    show_cars()

    if not cars:
        return

    try:
        choice = int(input("\nИзберете автомобил: "))

        if 1 <= choice <= len(cars):
            new_price = float(input("Нова цена: "))
            print(cars[choice - 1].change_price(new_price))
        else:
            print("Невалиден номер.")

    except ValueError:
        print("Невалидни данни.")


while True:
    print("\n===== АВТОСАЛОН =====")
    print("1. Добави автомобил")
    print("2. Покажи всички автомобили")
    print("3. Търси по марка")
    print("4. Сортирай по цена")
    print("5. Продай автомобил")
    print("6. Промени цена")
    print("7. Изход")

    choice = input("Изберете опция: ")

    if choice == "1":
        add_car()

    elif choice == "2":
        show_cars()

    elif choice == "3":
        search_by_brand()

    elif choice == "4":
        sort_by_price()

    elif choice == "5":
        sell_car()

    elif choice == "6":
        change_car_price()

    elif choice == "7":
        print("Изход от програмата...")
        break

    else:
        print("Невалиден избор!")
