import pytest
from selenium import webdriver
import settings
import random


def random_email():
    email = "olgabelova7" + str(random.randrange(100, 999)) + "@gmail.com"
    return email


def random_password():
    password = str(random.randrange(100000, 999999))
    return password


