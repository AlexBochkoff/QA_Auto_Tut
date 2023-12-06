import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

def test_github_login_negative():
    driver = webdriver.Firefox()
    driver.get("https://github.com/login")
    login_fld = driver.find_element(By.ID, "login_field")
    login_fld.send_keys('wrong email')

    pass_fld = driver.find_element(By.ID, "password")
    pass_fld.send_keys('wrong pass')

    creds_submit = driver.find_element(By.NAME, "commit")
    creds_submit.click()

    error_msg = driver.find_element(By.ID, "js-flash-container") # Replace with different idetifier e.g. Text of error

    time.sleep(5)

    assert error_msg is not None


#### test with tear_up/teardown but whout page object
@pytest.fixture
def github_login():
    # tear_up foreach
    # open the browser
    if CONFIG.BROWSER == "remote": 
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
    else:
        pass
        # use local 

    # navigate to login page
    driver.get("https://github.com/login")

    # return login page
    yield driver

    # tear_down foreach
    # close the browser --post set after EACH
    driver.quit()



def test_github_login_negative_fixture(github_login):
    login_fld = github_login.find_element(By.ID ,"login_field")
    login_fld.send_keys("wrong email")
    
    pass_fld = github_login.find_element(By.ID ,"password") 
    pass_fld.send_keys("wrong pass")

    # click button
    login_fld = github_login.find_element(By.NAME ,"commit")
    login_fld.click()
    
    # check error message
    error_msg = github_login.find_element(By.ID ,"js-flash-container") # replace with different identifier e.g. Text of error
    time.sleep(5)

    assert error_msg is not None


@pytest.fixture
def github_login_page_object():
    # tear_up foreach
    BROWSER_NAME = 'ff_slow'
    driver = BrowserProvider.get_driver(BROWSER_NAME)

    gitlab_login_page = GitHubUILoginPage(driver)
    gitlab_login_page.navigate_to_page()
    
    # return login page
    yield gitlab_login_page

    # tear_down foreach
    # close the browser --post set after EACH
    gitlab_login_page.close_browser()


def test_github_login_negative_page_object(github_login_page_object):
    github_login_page_object.try_to_login("kjasbdkjfsa", "ksjhdkjfsdf")

    assert github_login_page_object.check_login_error_message()


# ----------------------------------------------------------------------------------------------------------------------------

# def test_check_login_failed():
#     driver = webdriver.Chrome(service=Service(r"C:\\Users\\Oleksiy\\repos\\QAT\\QA_Auto_Tut\\src\\drivers\\chromedriver.exe")) # Driver for Chrome

#     driver.get("https://github.com/login")
#     elem = driver.find_element(By.ID, "login_field")
#     elem.send_keys("email")

#     elem = driver.find_element(By.ID, "password")
#     elem.send_keys("password")

#     elem.send_keys(Keys.RETURN)

#     assert driver.title == "GitHub"
#     driver.close()