import allure
from allure_commons.types import Severity
from selene import browser, by, be


def test_issue_text():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Issue в репозитории')
    allure.dynamic.story('Проверяем название issue в публичном репозитории GitHub')
    allure.dynamic.link("https://github.com", name="Testing")

    open_main_page()
    search_repository(repo='eroshenkoam/allure-example')
    follow_the_repository_link(repo='eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_name(name='Привет от 27го потока QA.GURU!!!')


@allure.step('Открываем главную страницу GitHub')
def open_main_page():
    browser.open('/')


@allure.step('Ищем репозиторий {repo}')
def search_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def follow_the_repository_link(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб issue')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие issue c названием {name}')
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).should(be.visible)
