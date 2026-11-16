class User:
    """Пользователь интернет-магазина."""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        self._email = value


class Product:
    """Базовый класс товара."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

    def shipping_cost(self):
        """Метод для переопределения в дочерних классах."""
        raise NotImplementedError("Method shipping_cost() must be implemented")


class DigitalProduct(Product):
    """Цифровой товар. Отличается от базового тем, что не требует физической доставки (стоимость доставки всегда 0)."""
    
    def shipping_cost(self):
        return 0.0


class PhysicalProduct(Product):
    """Физический товар. Отличается тем, что имеет вес, от которого зависит стоимость доставки."""
    
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def shipping_cost(self):
        return self.weight * 15.0


class Review:
    """Отзыв пользователя на товар."""
    
    def __init__(self, user, product, text, rating):
        self.user = user 
        self.product = product
        self.text = text
        self.rating = rating      
        
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    def is_positive(self):
        """Осмысленный метод: определяет, является ли отзыв положительным."""
        return self.rating >= 4


class Cart:
    """Корзина покупок пользователя."""
    
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.price for item in self.items)



if __name__ == "__main__":
    user1 = User("Nadia", "nadia@example.com")

    game = DigitalProduct("Honkai: Star Rail Pack", 1500)
    eva_foam = PhysicalProduct("EVA Foam 5mm", 800, weight=2.5)

    cart = Cart()
    cart.add(game)
    cart.add(eva_foam)
    
    print(f"Total cart price: {cart.total()}")
    
    total_shipping = 0
    for item in cart.items:
        cost = item.shipping_cost()
        print(f"Shipping for {item.name}: {cost}")
        total_shipping += cost
        
    print(f"Total shipping cost: {total_shipping}")
    
    review = Review(user1, eva_foam, "Отличный материал для крафта!", 5)
    print(f"Review by {review.user.username} is positive: {review.is_positive()}")