from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomerUserTests(TestCase):
    '''Тест пользователя'''

    def test_create_user(self):
        '''тест: можно создать пользователя'''
        User = get_user_model()
        user = User.objects.create_user(
            username='user1',
            email='user1@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        '''тест: можно создать суперпользователя'''
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@mail.ru',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@mail.ru')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTest(TestCase):
    '''Тест страницы регистрации'''

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        '''тест: страница регистрации существует и использует корректный шаблон'''
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Регистрация')
        self.assertNotContains(self.response, 'Этого не должно тут быть!')

    def test_signup_form(self):
        '''тест: используется форма CustomUserCreationForm и csrf токен'''
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        '''тест: url связан с корректным представлением'''
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )