import pytest
def inc(x):
    return x + 1

@pytest.mark.parametrize('a,b', [
    (1, 2),
    (3, 4),
    (5, 7),
])
def test_answer(a, b):
    assert inc(a) == b

def test_answer1():
    assert inc(4) == 5


class TestDemo:

    @pytest.fixture()
    def login(self):
        username = "chloe"
        return username

    def test_a(self, login):
        print(f'username = {login}')
        print('a')

    def test_b(self):
        print('b')

if __name__ == '__main__':
    pytest.main(['test_a.py::test_answer', '-v'])