from selenium import webdriver
import pytest
import json
import os.path


def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target


@pytest.fixture()
def browser():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://trading.alfa-one-capital.com/')
    yield driver
    driver.quit()

@pytest.fixture()
def first_name_data():
    first_name = load_config('resources/data_for_registration_form.json')
    return first_name['first_name']

@pytest.fixture()
def last_name_data():
    last_name = load_config('resources/data_for_registration_form.json')
    return last_name['last_name']

@pytest.fixture()
def phone_data():
    phone_data = load_config('resources/data_for_registration_form.json')
    return phone_data['phone']

@pytest.fixture()
def passwd_data():
    password = load_config('resources/data_for_registration_form.json')
    return password['password']
