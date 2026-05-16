class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.available = True

    def show_info(self):
        status = "Налична" if self.available else "Продадена"
        return f"{self.brand} {self.model} ({self.year}) - {self.price} лв. | Статус: {status}"

    def sell_car(self):
        if self.available:
            self.available = False
            return "Автомобилът беше успешно продаден."
        return "Автомобилът вече е продаден."

    def change_price(self, new_price):
        self.price = new_price
        return f"Новата цена е {self.price} лв."
