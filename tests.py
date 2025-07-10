from main import BooksCollector

import pytest

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
        # Метода get_books_rating нет в классе BooksCollector, заменен на get_books_genre
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверка метода add_new_book с использованием параметризации
    @pytest.mark.parametrize('book_add, expected_len',
    [
        [['Гарри Поттер и философский камень', 'Гарри Поттер и философский камень'], 1],
        [[''], 0],
        [['A' * 41], 0],
        [['A'], 1],
        [['A' * 40], 1],
    ]
    )   
    
    def test_add_new_book_add_books_edge_cases(self, book_add, expected_len):
        collector = BooksCollector()
        for name in book_add:
            collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_len
    
    # Проверка метода set_book_genre с использованием параметризации
    @pytest.mark.parametrize('book_set, genre_set, expected_genre',
    [
        ('Я, робот', ['Фантастика'], 'Фантастика'),
        ('Я, робот', ['Поэзия'], ''),
        ('Я, робот', ['Фантастика', 'Мультфильмы'], 'Мультфильмы'),
        ('', ['Фантастика'], None),  
    ]
    )
    def test_set_book_genre_edge_cases(self, book_set, genre_set, expected_genre):
        collector = BooksCollector()
        for genre_name in genre_set:
            collector.add_new_book(book_set)
            collector.set_book_genre(book_set, genre_name)
        assert collector.get_books_genre().get(book_set) == expected_genre

    #  Проверка метода get_book_genre с использованием параметризации
    @pytest.mark.parametrize('book_specific_genre, specific_genre, expected_specific_genre', 
    [
        ({'Дюна': 'Фантастика'}, 'Фантастика', ['Дюна']),
        ({'Дюна': 'Фантастика', '451° по Фаренгейту': 'Фантастика'}, 'Фантастика', ['Дюна', '451° по Фаренгейту']),
        ({'Оно': 'Ужасы', 'Дюна': 'Фантастика', 'Хоббит': 'Мультфильмы'}, 'Ужасы', ['Оно']),
        ({'Дюна': 'Фантастика'}, 'Поэзия', []),
        ({}, 'Фантастика', []),
        ({'Дюна': ''}, 'Фантастика', []),
    ]    
    )

    def test_get_books_with_specific_genre_edge_cases(self, book_specific_genre, specific_genre, expected_specific_genre):
        collector = BooksCollector()
        for name, genre in book_specific_genre.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(specific_genre) == expected_specific_genre

    # Проверка метода get_books_genre без параметризации
    def test_get_book_genre_one_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        assert collector.get_book_genre('Двенадцать стульев') == 'Комедии'

    # Проверка метода get_books_for_children через добавление в список валидных и невалидных объектов
    def test_get_books_for_children_valid_and_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Танец с драконами')
        collector.set_book_genre('Танец с драконами', 'Фантастика')
        collector.add_new_book('Муми-тролли')
        collector.set_book_genre('Муми-тролли', 'Мультфильмы')
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.add_new_book('')
        collector.set_book_genre('', 'Мультфильмы')
        collector.add_new_book('Невидимка')
        assert collector.get_books_for_children() == ['Танец с драконами', 'Муми-тролли']

    # Проверка метода add_book_in_favorites 
    def test_add_book_in_favorites_one_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Алиса в Стране чудес')
        collector.add_book_in_favorites('Алиса в Стране чудес')
        collector.add_book_in_favorites('Алиса в Стране чудес')
        assert collector.get_list_of_favorites_books() == ['Алиса в Стране чудес']

    @pytest.mark.parametrize('book_favorites, book_to_delete, expected_list', 
    [
        (['Алиса в Стране чудес'], 'Алиса в Стране чудес', []), 
        (['Алиса в Стране чудес', 'Муми-тролли'], 'Муми-тролли', ['Алиса в Стране чудес']),
    ]
    )
    
    # Проверка метода delete_book_from_favorites
    def test_delete_book_from_favorites_edge_cases(self, book_favorites, book_to_delete, expected_list):
        collector = BooksCollector()
        for name in book_favorites:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
            collector.delete_book_from_favorites(book_to_delete)
        assert collector.get_list_of_favorites_books() == expected_list

    # Проверка метода get_list_of_favorites_books с использованием фикстуры
    @staticmethod
    # С точки зрения best practice необходимо было вынести фикстуру вне класса/в conftest.py, но так как она используется только в одном методе, было решено оставить её внутри класса
    @pytest.fixture
    def favorites_collection():
        collector = BooksCollector()
        books = ['Девушка с татуировкой дракона', 'Автостопом по галактике', 'Винни-Пух и все-все-все']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        return collector
          
    def test_get_list_of_favorites_books_with_fixture(self, favorites_collection):
        list_of_favorites_books = favorites_collection.get_list_of_favorites_books()
        assert list_of_favorites_books == ['Девушка с татуировкой дракона', 'Автостопом по галактике', 'Винни-Пух и все-все-все']

    
  
