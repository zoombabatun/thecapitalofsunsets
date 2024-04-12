from __future__ import annotations

import sqlite3
from time import sleep

from urllib.parse import unquote

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import pathes


def get_element_text(driver: WebDriver, path: str) -> str:
    try:
        return driver.find_element(By.XPATH, path).text
    except NoSuchElementException:
        return ''


def move_to_element(driver: WebDriver, element: WebElement | WebDriver) -> None:
    try:
        webdriver.ActionChains(driver).move_to_element(element).perform()
    except StaleElementReferenceException:
        pass


def element_click(driver: WebDriver | WebElement, path: str) -> bool:
    try:
        driver.find_element(By.XPATH, path).click()
        return True
    except:
        return False

def main():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rests (
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL
        )
        ''')

    search_query = 'кафе'
    url = f'https://2gis.ru/n_novgorod/search/{search_query}'
    driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    element_click(driver, pathes.main_banner)
    element_click(driver, pathes.cookie_banner)
    count_all_items = int(get_element_text(driver, pathes.items_count))
    pages = round(count_all_items / 12 + 0.5)
    for _ in range(3):
        main_block = driver.find_element(By.XPATH, pathes.main_block)
        count_items = len(main_block.find_elements(By.XPATH, 'div'))
        # for item in range(1, count_items + 1):
        for item in range(1, count_items):
            if main_block.find_element(By.XPATH, f'div[{item}]').get_attribute('class'):
                continue
            item_clicked = element_click(main_block, f'div[{item}]/div/div[2]')
            if not item_clicked:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                element_click(main_block, f'div[{item}]/div/div[2]')
            title = get_element_text(driver, pathes.title)
            phone_btn_clicked = element_click(driver, pathes.phone_btn)
            phone = get_element_text(driver, pathes.phone) if phone_btn_clicked else ''
            move_to_element(driver, main_block)
            link = unquote(driver.current_url)
            address = get_element_text(driver, pathes.address)
            worktime = get_element_text(driver, pathes.worktime)
            cursor.execute('INSERT INTO Rests (name, phone, address) VALUES (?, ?, ?)',
                           (str(title), str(phone), str(address)))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element_click(driver, pathes.next_page_btn)
        sleep(0.5)
    connection.commit()
    connection.close()
    driver.quit()
if __name__ == '__main__':
    main()