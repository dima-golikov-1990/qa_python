import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Машина времени')

        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Машина времени', 'Фантастика'],
            ['Зов Ктулху', 'Ужасы'],
            ['Убийство в Восточном экспрессе', 'Детективы'],
            ['Рик и Морти', 'Мультфильмы'],
            ['Венецианский купец', 'Комедии']
        ]
    )
    def test_set_book_genre_check_book_genre(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.books_genre[book_name] == book_genre

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Машина времени', 'Фантастика'],
            ['Зов Ктулху', 'Ужасы'],
            ['Убийство в Восточном экспрессе', 'Детективы'],
            ['Рик и Морти', 'Мультфильмы'],
            ['Венецианский купец', 'Комедии']
        ]
    )
    def test_get_book_genre_check_genre_name(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Машина времени', 'Фантастика'],
            ['Зов Ктулху', 'Ужасы'],
            ['Убийство в Восточном экспрессе', 'Детективы'],
            ['Рик и Морти', 'Мультфильмы'],
            ['Венецианский купец', 'Комедии']
        ]
    )
    def test_get_books_with_specific_genre_check_book_name(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_with_specific_genre(book_genre) == [book_name]

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Машина времени', 'Фантастика'],
            ['Зов Ктулху', 'Ужасы'],
            ['Убийство в Восточном экспрессе', 'Детективы'],
            ['Рик и Морти', 'Мультфильмы'],
            ['Венецианский купец', 'Комедии']
        ]
    )
    def test_get_books_genre_check_genre_name(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre() == {book_name: book_genre}

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Машина времени', 'Фантастика'],
            ['Рик и Морти', 'Мультфильмы'],
            ['Венецианский купец', 'Комедии']
        ]
    )
    def test_get_books_for_children_check_book_name(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_for_children() == [book_name]

    def test_add_book_in_favorites_check_list_length(self):
        collector = BooksCollector()

        collector.add_new_book('Машина времени')
        collector.add_book_in_favorites('Машина времени')

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_check_list_length(self):
        collector = BooksCollector()

        collector.add_new_book('Машина времени')
        collector.add_book_in_favorites('Машина времени')
        collector.delete_book_from_favorites('Машина времени')

        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_check_book_name(self):
        collector = BooksCollector()

        collector.add_new_book('Рик и Морти')

        collector.add_book_in_favorites('Рик и Морти')

        assert collector.favorites[0] == 'Рик и Морти'
