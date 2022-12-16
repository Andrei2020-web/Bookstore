from django.test import TestCase
from django.urls import reverse, resolve
from .models import Book, Review
from .views import BookListView, BookDetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


class BookTests(TestCase):
    '''Тест книг'''

    def setUp(self):
        self.book = Book.objects.create(
            title='Python. Разработка на основе тестирования',
            author='Персиваль Гарри',
            price='2500',
        )
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@mail.ru',
            password='%%%%%%%%',
        )
        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='Хорошая книга.'
        )
        self.special_permission = Permission.objects.get(
            codename='special_status')

    def test_book_listing(self):
        '''тест: содержимого книги'''
        self.assertEqual(self.book.title,
                         'Python. Разработка на основе тестирования')
        self.assertEqual(self.book.author, 'Персиваль Гарри')
        self.assertEqual(self.book.price, '2500')

    def test_string_representation(self):
        '''тест: строкового представления книги'''
        self.assertEqual(str(self.book),
                         'Python. Разработка на основе тестирования')

    def test_book_list_view_for_logged_in_user(self):
        '''тест: представления списка книг для зарегистрированного пользователя'''
        self.client.login(email='reviewuser@mail.ru', password='%%%%%%%%')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response,
                            'Python. Разработка на основе тестирования')

    def test_book_list_view_for_logged_out_user(self):
        '''тест: представления списка книг для незарегистрированного пользователя'''
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Войти')

    def test_book_detail_view_with_permissions(self):
        '''тест: представления книги c разрешениями'''
        self.client.login(email='reviewuser@mail.ru', password='%%%%%%%%')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response,
                            'Python. Разработка на основе тестирования')
        self.assertContains(response, 'Отзывы')
        self.assertContains(response, 'Хорошая книга.')

    def test_book_list_url_resolves_book_list_view(self):
        '''тест: url страницы списка книг разрешает вызов функции представления'''
        view = resolve(reverse('book_list'))
        self.assertEqual(
            view.func.__name__,
            BookListView.as_view().__name__
        )

    def test_book_url_resolves_book_view(self):
        '''тест: url страницы книги разрешает вызов функции представления книги'''
        view = resolve(self.book.get_absolute_url())
        self.assertEqual(
            view.func.__name__,
            BookDetailView.as_view().__name__
        )
