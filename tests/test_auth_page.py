
# python -m pytest -v --driver Chrome --driver-path tests\chromedriver.exe tests\test_auth_page.py

from selenium import webdriver
from pages.auth_page import AuthPage
from selenium import webdriver
import time
from settigs import *


def test_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email(valid_email)
   page.enter_pass(valid_password)
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() != '/all_pets', "login error"

   time.sleep(5) #задержка для учебных целей