from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

from settigs import *

def test_title_contains():
    try:
        driver = webdriver.Chrome()
        driver.get('http://petfriends.skillfactory.ru/login')
        driver.maximize_window()
        # Вводим email
        driver.find_element(By.ID, 'email').send_keys(valid_email)
        # Вводим пароль
        driver.find_element(By.ID, 'pass').send_keys(valid_password)
        time.sleep(2)
        # Нажимаем на кнопку входа в аккаунт
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # Активируем ожидание, пока на странице не появится заголовок "PetFriends"
        # WebDriverWait(driver, 10).until(EC.title_contains("PetFriends"))
        # Нажимаем на кнопку Мои питомцы
        time.sleep(5)
        driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()
        """
          Мы объявили три переменные, в которых записали все найденные элементы на странице:
          в images — все картинки питомцев, в names — все их имена, в descriptions — все виды и возрасты.
          """
        images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')

        descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

        for i in range(len(names)):
            assert images[i].get_attribute('src') != ''  # на странице нет питомцев без фото
            assert names[i].text != ''  # на странице нет питомцев без Имени
            assert descriptions[i].text != ''  # на странице нет питомцев с пустым полем для указания Породы и возраста
            assert ', ' in descriptions[i]  # проверяем, что между породой и лет есть запятая (значит есть оба значения)
            parts = descriptions[i].text.split(", ")  # Создаём список, где разделитель значений - запятая
            assert len(parts[0]) > 0  # Проверяем, что длина текста в первой части списка и
            assert len(parts[1]) > 0  # ...и во второй > 0, значит там что-то да указано! Если нет -> FAILED!


    finally:

        time.sleep(10)
        driver.close()
        driver.quit()