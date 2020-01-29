# from django.test import TestCase
from hypothesis.extra.django import TestCase
from hypothesis import given
import hypothesis.strategies as st
from accounts.forms import SignUpForm


class UserCreationFormTest(TestCase):

    def test_valid_form(self):
        data = {'username': 'tom', 'email': 'tom@vp.pl', 'password1': 'prorok29', 'password2': 'prorok29'}
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())

    @given(st.sampled_from([
        {'username': 'tom', 'email': 'tom@vp.pl', 'password1': 'prorok29', 'password2': 'prorok'},
        {'username': '', 'email': 'tom@vp.pl', 'password1': 'prorok29', 'password2': 'prorok29'},
        {'username': 'tom', 'email': '', 'password1': 'prorok29', 'password2': 'prorok'},
        {'username': 'tom', 'email': 'tomvp.pl', 'password1': 'prorok29', 'password2': 'prorok29'},
        {'username': 'tom', 'email': 'tom@vp.pl', 'password1': '', 'password2': 'prorok'},
        {'username': 'tom', 'email': 'tom@vp.pl', 'password1': 'prorok29', 'password2': 'prorok'},
        {'username': 'tom', 'email': 'tom@vp.pl', 'password1': 'abcd', 'password2': 'abcd'}
    ]))
    def test_invalid_form(self, data):
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
