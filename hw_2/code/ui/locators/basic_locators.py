"""Тут разбиваем локаторы на классы, в соответсвием их местоположением на странице"""
from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOG_IN = (By.XPATH, '//div[contains(@class, "response") and contains(text(), "Войти")]')


class MainPageLocators(object):
    CAMPAIGNS = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    AUDITORY = (By.XPATH, '//a[@href="/segments"')


class LoginLocators(object):
    LOG_IN_EMAIL = (By.XPATH, '//input[@name="email"]')
    LOG_IN_PASSWORD = (By.XPATH, '//input[@type="password"]')
    AUTH_FORM_LOG_IN = (By.XPATH, '//div[@class="authForm-module-button-2G6lZu"]')
    LOG_IN_FAILED = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')


class CreateCampaign(object):
    CREATE_NEW_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    TRAFFIC_BUTTON = (By.XPATH, '//div[contains(text(), "Трафик")]')
    CAMPAIGN_LINK = (By.XPATH, '//input[contains(@placeholder, "Введите ссылку")]')
    CLEAR_BUTTON = (By.XPATH, '//div[contains(@class, "input__clear")]')
    CAMPAIGN_NAME = (By.XPATH, '//div[contains(@class, "campaign-name")]//input')
    BANNER_BUTTON = (By.XPATH, '//span[contains(text(), "Баннер")]')
    DAILY_BUDGET = (By.XPATH, '//input[contains(@data-test, "budget-per_day")]')
    TOTAL_BUDGET = (By.XPATH, '//input[contains(@data-test, "budget-total")]')
    LOAD_IMAGE_BUTTON = (By.XPATH, '//input[contains(@data-test,"240")]')
    NUM_OF_CAMPAIGNS = (
        By.XPATH, '//div[contains(@class, "dashboard-module-pagination")]//span[3][contains(text(), 30)]'
    )


class CreateSegment(object):
    CREATE_FIRST_SEGMENT = (By.XPATH, '//a[contains(text(), "Создайте")]')
    CREATE_NEW_SEGMENT = (By.XPATH, '//div[contains(text(), "Создать")]')
    APP_AND_GAMES = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    PLAYED_AND_PAID = (By.XPATH, '//span[contains(text(), "Игравшие и платившие в платформе")]')
    PAID_ON_PLATFORM = (By.XPATH, '//span[contains(text(), "Платившие в платформе")]')
    ADD_SEGMENT = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    NEW_SEGMENT_NAME = (By.XPATH, '//input[@maxlength= "60"]')
    CREATE_CURRENT_SEGMENT = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    ALL_SEGMENTS = (By.XPATH, '//a[@href="/segments"]')
    DELETE_SEGMENT = (By.XPATH, '//div[contains(text(), "Удалить")]')
