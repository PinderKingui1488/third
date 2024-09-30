from src.category import Category
from src.product import Product, LawnGrass, Smartphone


def test_product_creation() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_getter() -> None:
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 200000.0
    assert product.price == 200000.0
    product.price = -100
    assert product.price == 200000.0


def test_category_creation() -> None:
    category = Category("Смартфоны", "Лучшие смартфоны 2023 года", [])
    assert category.name == "Смартфоны"
    assert category.description == "Лучшие смартфоны 2023 года"
    assert len(category.products) == 0


def test_add_product_fail() -> None:
    category = Category("Смартфоны", "Лучшие смартфоны 2023 года", [])
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    try:
        category.add_product(product)
    except Exception as e:
        assert type(e) is TypeError



if __name__ == "__main__":
    test_product_creation()
    test_price_setter_getter()
    test_category_creation()



    def test_str(category, Sacred_Relic):
        assert str(Sacred_Relic) == " Radiance, 3400. Остаток: 4 шт."
        assert str(category) == "айтемы, количество продуктов: 3 шт."


    def test_add(Sacred_Relic):
        product = Product.new_product({"name": "name1", "description": "-", "price": 140, "quantity": 3})
        assert Sacred_Relic + product == 442

    def test_init3(smartphone):
            assert smartphone.name == "Ring of Tarrasque"
            assert smartphone.description == "предмет, который можно купить в ПОДТОЙНАЯ лавке, в разделе разное."
            assert smartphone.price == 1800
            assert smartphone.quantity == 1
            assert smartphone.efficiency == 12
            assert smartphone.model == "7.37"
            assert smartphone.memory == 4
            assert smartphone.color == "RED"

    def test_init4(lawn_grass):
            assert lawn_grass.name == "Recipe of Tarrasque"
            assert lawn_grass.description == "это предмет , который сам по себе ничего не делает."
            assert lawn_grass.price == 600
            assert lawn_grass.quantity == 1
            assert lawn_grass.country == "Warcraft"
            assert lawn_grass.germination_period == "after 40 minute"
            assert lawn_grass.color == "yellow"
