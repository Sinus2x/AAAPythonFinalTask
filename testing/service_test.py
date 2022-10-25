from service import bake, delivery_pizza, pickup
from unittest.mock import MagicMock, patch, call


@patch('builtins.print')
def test_bake(mocked_print):
    pizza = MagicMock()
    pizza.__class__.__name__ = 'Margherita'
    pizza.size = 'L'
    bake.__wrapped__(pizza)
    assert mocked_print.mock_calls == [call('Margherita of size L')]


@patch('random.randint')
@patch('builtins.print')
def test_delivery(mocked_print, randint_mock):
    randint_mock.return_value = 1

    pizza = MagicMock()
    pizza.__class__.__name__ = 'Margherita'
    pizza.size = 'L'

    delivery_pizza(pizza)
    assert mocked_print.mock_calls == [call('Margherita of size L'),
                                       call('bake - 1 с'),
                                       call('🛵 Доставили за 1 с!')]


@patch('random.randint')
@patch('builtins.print')
def test_pickup(mocked_print, randint_mock):
    randint_mock.return_value = 1

    pizza = MagicMock()
    pizza.__class__.__name__ = 'Margherita'
    pizza.size = 'L'

    pickup(pizza)
    assert mocked_print.mock_calls == [call('Margherita of size L'),
                                       call('bake - 1 с'),
                                       call('🏠 Забрали за 1 с!')]