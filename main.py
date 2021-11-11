import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def click(driver, id = "NextButton"):
    button = driver.find_element_by_id(id)
    button.click()

def main():
    # Initialize webdriver
    driver = webdriver.Chrome('/Users/alecgoedinghaus/Downloads/chromedriver')
    url = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7?utm_source=BP06158+UCLA+COVID-19+Symptom+Monitoring+Survey+Reminder+Notification&utm_medium=email&utm_campaign=&utm_content=UCLA+COVID-19+Symptom+Monitoring+and+Vaccination+Verification+System+Survey"
    driver.get(url)

    # Read MyUCLA info
    with open('credentials.txt') as f:
        lines = f.readlines()
    
    username = lines[0]
    password = lines[1]

    # First Screen
    time.sleep(1)
    click(driver, "QID3-2-label")
    click(driver)
    time.sleep(1)

    # Log onto MyUCLA
    time.sleep(3)
    text = driver.find_element_by_id("logon")
    text.send_keys(username)

    text = driver.find_element_by_id("pass")
    text.send_keys(password)

    text.send_keys(Keys.TAB)
    text.send_keys(Keys.ENTER)

    # time.sleep(3)
    # button = driver.find_element_by_class_name("primary-button")
    # button.click()
    time.sleep(15)

    # Student Confirmation Page
    click(driver)
    time.sleep(1)

    # Survey Information Page
    click(driver)
    time.sleep(1)

    # On Campus Expectations
    click(driver, "QID221-15-label")
    click(driver)
    time.sleep(1)

    # Login Information Confirmation
    click(driver)
    time.sleep(1)

    # Alt Email Page
    click(driver)
    time.sleep(1)

    # Vaccine Confirmation
    click(driver)
    time.sleep(1)

    # 24hr Symptoms
    click(driver, "QID2-1-label")
    click(driver)
    time.sleep(1)

    # Positive Covid Test
    click(driver, "QID3-2-label")
    click(driver)
    time.sleep(1)

    # Current Isolation Status
    click(driver, "QID12-2-label")
    click(driver)
    time.sleep(5)

    # Goodbye
    driver.quit()

main()