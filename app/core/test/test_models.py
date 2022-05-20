from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating anew user with an email is successful"""
        email = 'test@eco.sa'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        email = 'test@ECO.SA'
        user = get_user_model().objects.create_user(
            email=email,
            password='1234'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.user = get_user_model() \
                .objects.create_user(
                email='',
                password='1234'
            )

    def test_create_new_supper_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='w@nwa.sdn',
            password='1234'
        )
        self.assertEqual(user.is_superuser, True)
