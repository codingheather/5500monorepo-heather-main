# To check test coverage:
# pytest --cov=src test_main.py
# To check it on web:
# coverage html
from ..src.main import *



def test_first_api():
    assert first_api()
    print(first_api())


def test_first_apiV2():
    assert first_apiV2('foobar')["msg"] == "foobar"
    print(first_apiV2('foobar'))


def test_first_apiV3():
    assert first_apiV3("The Sun Also Rises")["msg"] == "The Sun Also Rises"
    print(first_apiV3("The Sun Also Rises"))


def test_first_apiV4():
    assert first_apiV4("foobar", "The Sun Also Rises")["category"] == "foobar"
    assert first_apiV4("foobar", "The Sun Also Rises")["author"] == "The Sun Also Rises"
    print(first_apiV4("foobar", "The Sun Also Rises"))


def test_first_apiV5():
    assert first_apiV5("{'tittle': 'Antifragile' , 'author' : 'Nassem Talib', 'category': 'non-fiction'}")
    print(first_apiV5("{'tittle': 'Antifragile' , 'author' : 'Nassem Talib', 'category': 'non-fiction'}"))


def test_first_apiV6():
    new_book = Book(author = 'Nassem Talib', title = 'Antifragile', category = 'non-fiction')
    assert first_apiV6(new_book, "Emma")
    print(first_apiV6(new_book, "Emma"))


def test_first_apiV7():
    assert first_apiV7("Emma")
    print(first_apiV7("Emma"))