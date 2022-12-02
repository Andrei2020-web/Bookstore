from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomePageTest(SimpleTestCase):
    '''тест домашней страницы'''

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        '''тест: домашняя страница существует'''
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        '''тест: домашняя страница использует корректный шаблон'''
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        '''тест: домашняя страница содержит правильный html код'''
        self.assertContains(self.response, 'Домашняя страница')

    def test_homepage_does_not_contain_incorrect_html(self):
        '''тест: домашняя страница не содержит неправильный html код'''
        self.assertNotContains(self.response, 'Этого не должно тут быть')

    def test_homepage_url_resolves_homepageview(self):
        '''тест: url домашней страницы разрешает вызов функции homepageview'''
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTest(SimpleTestCase):
    '''Тест страницы о программе'''

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        '''тест: страница о программе существует'''
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        '''тест: страница о программе использует корректный шаблон'''
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        '''тест: страница о программе содержит правильный html код'''
        self.assertContains(self.response, 'О программе')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        '''тест: страница о программе не содержит неправильный html код'''
        self.assertNotContains(self.response, 'Этого не должно тут быть')

    def test_aboutpage_url_resolves_aboutpageview(self):
        '''тест: url страницы о программе разрешает вызов функции aboutpageview'''
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )