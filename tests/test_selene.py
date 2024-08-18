from selene import browser, by, be


def test_issue_text():
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('Привет от 27го потока QA.GURU!!!')).should(be.visible)
