import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click(driver, id="NextButton"):
    button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, id)))
    button.click()


def main():
    # Initialize webdriver
    driver = webdriver.Firefox()
    # straight to student survey
    url = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_2fy4RuUi5Izpreu"
    driver.get(url)

    username = os.environ['UCLA_USER']
    password = os.environ['UCLA_PASS']

    text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "logon")))
    text.send_keys(username)

    text = driver.find_element(By.ID, "pass")
    text.send_keys(password)

    text.send_keys(Keys.TAB)
    text.send_keys(Keys.ENTER)

    # wait for DUO to get verified
    WebDriverWait(driver, 30).until(EC.title_is('UCLA Symptom Monitoring'))

    # Student Confirmation Page
    click(driver)

    # Survey Information Page
    click(driver)

    # On Campus Expectations
    click(driver, "QID221-15-label")
    click(driver)

    # Login Information Confirmation
    click(driver)

    # Alt Email Page
    click(driver)

    # Vaccine Confirmation
    click(driver)

    # 24hr Symptoms
    click(driver, "QID2-1-label")
    click(driver)

    # Positive Covid Test
    click(driver, "QID3-2-label")
    click(driver)

    # Current Isolation Status
    click(driver, "QID12-2-label")
    click(driver)

    # Goodbye
    driver.quit()


if __name__ == "__main__":
    main()
