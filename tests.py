import pytest
from test_data import (
    add_new_book_length_cases,
    add_new_book_duplicate_case,
    set_book_genre_cases,
    get_books_with_specific_genre_valid_cases,
    get_books_with_specific_genre_invalid_case,
    delete_book_from_favorites_cases,
    get_list_of_favorites_books_cases
)

# Проверка граничных значений длины книги в методе add_new_book
@pytest.mark.parametrize('book_add, expected_len', add_new_book_length_cases)
def test_add_new_book_length_validation(collector, book_add, expected_len):
    for name in book_add:
        collector.add_new_book(name)
    assert len(collector.get_books_genre()) == expected_len

# Проверка дублирующих значений в методе add_new_book
def test_add_new_book_duplicate(collector):
    book_add, expected_len = add_new_book_duplicate_case
    for name in book_add:
        collector.add_new_book(name)
    assert len(collector.get_books_genre()) == expected_len

# Проверка метода set_book_genre с использованием параметризации
@pytest.mark.parametrize('book_set, genre_set, expected_genre', set_book_genre_cases)
def test_set_book_genre_edge_cases(collector, book_set, genre_set, expected_genre):
    for genre_name in genre_set:
        collector.add_new_book(book_set)
        collector.set_book_genre(book_set, genre_name)
    assert collector.get_books_genre().get(book_set) == expected_genre

# Проверка метода get_book_genre 
def test_get_book_genre_one_valid_book(collector):
    collector.add_new_book('Двенадцать стульев')
    collector.set_book_genre('Двенадцать стульев', 'Комедии')
    assert collector.get_book_genre('Двенадцать стульев') == 'Комедии'

# Проверка метода get_books_with_specific_genre с валидными значениями
@pytest.mark.parametrize('book_specific_genre, specific_genre, expected', get_books_with_specific_genre_valid_cases)
def test_get_books_with_specific_genre_valid(collector, book_specific_genre, specific_genre, expected):
    for name, genre in book_specific_genre.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    assert collector.get_books_with_specific_genre(specific_genre) == expected

# Проверка метода get_books_with_specific_genre с невалидными значениями
def test_get_books_with_specific_genre_invalid(collector):
    book_specific_genre, specific_genre, expected = get_books_with_specific_genre_invalid_case
    for name, genre in book_specific_genre.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    assert collector.get_books_with_specific_genre(specific_genre) == expected

# Проверка метода get_books_for_children с валидными значениями
def test_get_books_for_children_one_valid(collector):
    collector.add_new_book('Муми-тролли')
    collector.set_book_genre('Муми-тролли', 'Мультфильмы')
    assert collector.get_books_for_children() == ['Муми-тролли']

# Проверка метода get_books_for_children с невалидным значением по возрастному рейтингу
def test_get_books_for_children_with_age_rating(collector):
    collector.add_new_book('Убийство в Восточном экспрессе')
    collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
    assert collector.get_books_for_children() == []

# Проверка метода add_book_in_favorites с одним валидным значением
def test_add_book_in_favorites_one_valid_book(collector):
    collector.add_new_book('Алиса в Стране чудес')
    collector.add_book_in_favorites('Алиса в Стране чудес')
    collector.add_book_in_favorites('Алиса в Стране чудес')
    assert collector.get_list_of_favorites_books() == ['Алиса в Стране чудес']

# Проверка метода delete_book_from_favorites с использованием параметризации
@pytest.mark.parametrize('book_favorites, book_to_delete, expected_list', delete_book_from_favorites_cases)
def test_delete_book_from_favorites(collector, book_favorites, book_to_delete, expected_list):
    for name in book_favorites:
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
    collector.delete_book_from_favorites(book_to_delete)
    assert collector.get_list_of_favorites_books() == expected_list

# Проверка метода get_list_of_favorites_books с использованием параметризации
def test_get_list_of_favorites_books(collector):
    for name in get_list_of_favorites_books_cases:
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
    assert collector.get_list_of_favorites_books() == get_list_of_favorites_books_cases
    