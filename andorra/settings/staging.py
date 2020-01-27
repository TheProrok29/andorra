# flake8: noqa
import django_heroku
from .development import *

django_heroku.settings(locals(), test_runner=False)
