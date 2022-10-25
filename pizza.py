from typing import Literal, Generator, cast


possible_sizes = Literal['L', 'XL']


class Pizza:
    """
    Хотел сделать абстрактный класс, но, кажется,
    здесь достаточно обычного базового.
    """
    _components = ['tomato_sauce', 'mozzarella']

    def __init__(
            self,
            size: Literal['L', 'XL', 'l', 'xL', 'Xl', 'xl'] = 'L'
    ) -> None:
        """
        Буду исходить из того, что после инстанса размер нельзя изменить,
        будто пицца уже заказана.
        И сделаю size приватным
        """
        assert size.upper() in ['L', 'XL'], "The size doesn't exist"
        self.__size = size.upper()

    @property
    def size(self) -> Literal['L', 'XL']:
        return cast(possible_sizes, self.__size)

    @property
    def emoji(self) -> str:
        raise NotImplementedError  # ругаемся, если не задали эмодзи для пиццы

    @classmethod  # type: ignore
    @property
    def components(cls) -> list[str]:
        """
        Проигнорировал сообщение mypy,
        поскольку композиция декораторов
        classmethod + property - единственный способ сделать
        геттер для аттрибута класса с защищённым доступом через точку
        (без вызова)
        """
        return cls._components

    def __iter__(self) -> Generator:
        for i, ingr in enumerate(self._components):
            yield f'ingridient {i + 1}', ingr

    def __eq__(self, other) -> bool:
        return self.__class__.__name__ == other.__class__.__name__


class Margherita(Pizza):
    emoji = '🧀'
    _components = Pizza._components + ['tomatoes']


class Pepperoni(Pizza):
    emoji = '🍕'
    _components = Pizza._components + ['pepperoni']


class Hawaiian(Pizza):
    emoji = '🍍'
    _components = Pizza._components + ['chicken'] + ['pineapples']


if __name__ == '__main__':
    m = Margherita()
    p = Pepperoni()
    print(m.components)
    print(p.emoji)
    print(dict(Margherita()))
