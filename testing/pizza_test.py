import pytest
from pizza import Margherita, Pepperoni, Hawaiian, Pizza


def test_dict():
    m = Margherita()
    n_components = len(m.components)

    keys = [f'ingridient {i}' for i in range(1, n_components + 1)]
    assert dict(m) == dict(zip(keys, m.components))


def test_eq():
    m = Margherita()
    p = Pepperoni()
    assert (m == p) is False


def test_instance():
    m = Margherita()
    p = Pepperoni()
    h = Hawaiian()

    assert m.components == ['tomato_sauce', 'mozzarella'] + ['tomatoes']
    assert p.components == ['tomato_sauce', 'mozzarella'] + ['pepperoni']
    assert h.components == ['tomato_sauce', 'mozzarella'] + ['chicken']\
           + ['pineapples']


def test_class_attr():
    assert Margherita.components == \
           ['tomato_sauce', 'mozzarella'] + ['tomatoes']
    assert Pepperoni.components == \
           ['tomato_sauce', 'mozzarella'] + ['pepperoni']
    assert Hawaiian.components == \
           ['tomato_sauce', 'mozzarella'] + ['chicken'] + ['pineapples']


def test_emoji():
    assert Margherita.emoji == '🧀'
    assert Pepperoni.emoji == '🍕'
    assert Hawaiian.emoji == '🍍'


def test_size_set():
    p = Pizza()
    with pytest.raises(AttributeError):
        p.size = 'L'


def test_size_instance():
    with pytest.raises(AssertionError):
        Pizza('xxl')


def test_lowercase():
    p = Pizza('l')
    assert p.size == 'L'


