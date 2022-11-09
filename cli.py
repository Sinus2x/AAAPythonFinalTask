import click
from pizza import Pizza, possible_sizes
from typing import cast, Iterable
from service import delivery_pizza, pickup


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Готовит и доставляет пиццу
    """

    # не использую тернарный оператор - mypy плохо работает с ним
    if delivery:
        size = 'XL'
    else:
        size = 'L'
    size = cast(possible_sizes, size)

    # ищем нужный класс пиццы, чтобы создать соответствующий заказ
    for pizza_class in Pizza.__subclasses__():
        if pizza_class.__name__.lower() == pizza.lower():
            if delivery:
                delivery_pizza(pizza_class(size))
            else:
                pickup(pizza_class())


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for pizza_class in Pizza.__subclasses__():
        pizza_line = f'- {pizza_class.__name__} {pizza_class.emoji}: '

        ingridients = cast(Iterable[str], pizza_class.components)  # mypy fix

        pizza_line = pizza_line + ', '.join(ingridients)
        print(pizza_line)


if __name__ == '__main__':
    cli()


