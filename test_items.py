from selenium.webdriver.common.by import By
import time



def test_guest_should_see_the_trash_button_(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(2)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary")
    assert len(buttons) > 0, 'button not found'