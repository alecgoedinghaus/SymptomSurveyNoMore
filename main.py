from os import environ
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


def click(driver, id=None):
    if id is None:
        id = "NextButton"

    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, id)))
    try:
        button.click()  # I found this works better than ActionChain/scrolling solutions
    except ElementNotInteractableException:
        print("scroll error, attempting manual")
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(button).perform()
        # https://stackoverflow.com/questions/44777053/selenium-movetargetoutofboundsexception-with-firefox
        button.click()
    except:
        print("other error")


def main():
    # Initialize webdriver
    driver = None
    try:
        driver = webdriver.Chrome()
    except:
        print('no chrome driver found')
    if not driver:
        try:
            driver = webdriver.Firefox()
        except:
            print('no firefox driver found')

    if not driver:
        print('no supported driver found')
        return

    # straight to student survey
    url = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_aeH9BFhYVjkYTsO"
    driver.get(url)

    username = environ['UCLA_USER']
    password = environ['UCLA_PASS']

    text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "logon")))
    text.send_keys(username)

    text = driver.find_element(By.ID, "pass")
    text.send_keys(password)

    text.send_keys(Keys.TAB)
    text.send_keys(Keys.ENTER)

    # wait for DUO to get verified
    WebDriverWait(driver, 30).until(EC.title_is('UCLA Symptom Monitoring'))

    # This is student form
    click(driver)

    # Your login information and clearance status
    click(driver)

    # Do you need to update your status? (you have indicated not completely remote)
    click(driver, "QID215-2-label")  # no
    click(driver)

    # Do you need clearance
    click(driver, "QID207-4-label")  # yes
    click(driver)

    # 24hr Symptoms
    try:
        click(driver, "QID2-1-label")
        click(driver)
    except ElementClickInterceptedException:    # Kind of hacky but should work
        driver.quit()
        main()

    # Current Isolation Status
    click(driver, "QID12-2-label")
    click(driver)

    # Music/theater testing requirements
    # try:
    #     click(driver, "QID289-2-label")
    #     click(driver)
    # except TimeoutException:
    #     pass

    # Recent negative COVID test
    try:
        click(driver, "QID293-1-label")
        click(driver)
    except TimeoutException:
        pass

    # Goodbye
    sleep(1)
    driver.quit()


if __name__ == "__main__":
    main()