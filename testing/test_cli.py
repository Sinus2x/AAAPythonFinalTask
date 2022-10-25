from click.testing import CliRunner
from cli import cli
from unittest.mock import patch


@patch('random.randint')
def test_command_order_delivery(randint_mocked):
    randint_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "Margherita", "--delivery"])
    assert result.exit_code == 0

    correct = 'Margherita of size XL\nbake - 1 с\n🛵 Доставили за 1 с!\n'
    assert result.output == correct


@patch('random.randint')
def test_command_order(randint_mocked):
    randint_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "Margherita"])
    assert result.exit_code == 0

    correct = 'Margherita of size L\nbake - 1 с\n🏠 Забрали за 1 с!\n'
    assert result.output == correct


def test_command_menu():
    runner = CliRunner()
    result = runner.invoke(cli, ["menu"])
    assert result.exit_code == 0

    margherita = '- Margherita 🧀: ' + 'tomato_sauce, mozzarella, tomatoes'
    pepperoni = '- Pepperoni 🍕: ' + 'tomato_sauce, mozzarella, pepperoni'
    hawaiian = '- Hawaiian 🍍: ' + 'tomato_sauce, mozzarella, chicken,' \
                                  ' pineapples'
    correct = '\n'.join([margherita, pepperoni, hawaiian]) + '\n'
    assert result.output == correct
