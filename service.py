from pizza import Pizza
from fp import log


@log
def bake(pizza: Pizza) -> None:
    """Готовим пиццу"""
    print(f'{pizza.__class__.__name__} of size {pizza.size}')
    return


@log('🛵 Доставили за {} с!')
def delivery_pizza(pizza: Pizza) -> None:
    """Доставляет пиццу"""
    bake(pizza)
    return


@log('🏠 Забрали за {} с!')
def pickup(pizza: Pizza) -> None:
    bake(pizza)
    return
