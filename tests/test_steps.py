import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Roman Tropin')
@allure.link('https://github.com', name='Testing')
@allure.feature('Issue в репозитории')
@allure.story('Проверяем название issue в публичном репозитории GitHub')
def test_issue_text():
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб issue'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие issue c названием "Привет от 27го потока QA.GURU!!!"'):
        browser.element(by.partial_text('Привет от 27го потока QA.GURU!!!')).should(be.visible)
