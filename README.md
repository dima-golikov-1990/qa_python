# qa_python

### Описание проекта:

**BooksCollector** - приложение, которое позволяет установить жанр книг и добавить их в избранное.

### Использованные библиотеки:

**pytest** - для написания и запуска юнит-тестов.


### Список юнит-тестов: 

* **test_add_new_book_add_one_book** - проверка, что после добавления книги длина списка книг стала равной 1
* **test_add_new_book_add_book_with_incorrect_name_length** - проверка, что книга с некорректной длиной названия не добавляется в словарь
* **test_add_new_book_add_book_with_correct_name_length** - проверка, что книга с корректной длиной названия добавляется в словарь
* **test_set_book_genre_check_book_genre** - проверка, что у книги жанр, который ранее ей был присвоен
* **test_get_book_genre_check_genre_name** - проверка, что по названию книги метод get_book_genre возвращает соответствующий ей жанр
* **test_get_books_with_specific_genre_check_book_name** - проверка, что по жанру метод get_books_with_specific_genre возвращает соответствующую ему книгу
* **test_get_books_genre_check_dictionary_elements** - проверка, что метод get_books_genre выдаёт словарь с добавленными в него книгами и жанрами
* **test_get_books_for_children_check_book_name** - проверка, что в списке книг для детей книги соответствующих жанров 
* **test_add_book_in_favorites_check_that_book_in_favorites** - проверка, что после добавления книги в Избранное можно вывести список Избранное с помощью метода get_list_of_favorites_books
* **test_delete_book_from_favorites_check_list_length** - проверка, что после удаления книги из Избранного данный список стал пустым
* **test_get_list_of_favorites_books_check_book_name** - проверка, что в Избранное добавлена книга с указанным названием
