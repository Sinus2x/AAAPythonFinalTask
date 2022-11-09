from fp import log
from unittest.mock import patch, call


@patch('builtins.print')
@patch('fp.random.randint')
def test_non_parametric_log(randint_mock, print_mock):
    @log
    def decorated():
        pass

    randint_mock.return_value = 1
    decorated()
    assert print_mock.mock_calls == [call('decorated - 1 с')]


@patch('builtins.print')
@patch('fp.random.randint')
def test_parametric_log(randint_mock, print_mock):
    @log('time {} с')
    def decorated():
        pass

    randint_mock.return_value = 1
    decorated()
    assert print_mock.mock_calls == [call('time 1 с')]
