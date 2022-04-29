from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR LINKEDIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"
chrome_driver_path = "/Users/burcualakus/Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_up_page_nav = driver.find_element(By.CSS_SELECTOR,
                                       "body > div.base-serp-page > header > nav > div > a.nav__button-secondary")
sign_up_page_nav.click()

time.sleep(5)
email_input = driver.find_element(By.CSS_SELECTOR, "#username")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys(PASSWORD)
sign_in_button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
sign_in_button.click()

time.sleep(5)
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
main_window_id = driver.current_window_handle

# visit all jobs
for job in jobs_list:
    job.click()
    time.sleep(2)

    try:
        easy_apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
        easy_apply_button.click()
        time.sleep(5)
        submit_button = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button .artdeco-button__text")
        # if easy apply is only one step
        if submit_button.text == 'Submit application':
            add_number = driver.find_element(By.CSS_SELECTOR, '.fb-single-line-text input')
            # check if the text field is empty, only then enter your number
            if add_number.get_attribute("value") == "":
                add_number.send_keys(PHONE)
            # submit_button.click()
            print('Applied')
            time.sleep(5)

            try:
                closing_prev_app = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss svg')
                closing_prev_app.click()
            except NoSuchElementException:
                dismiss_screen = driver.find_element(By.CSS_SELECTOR, '.artdeco-toast-item__dismiss svg')
                dismiss_screen.click()
        else:
            # in-case the submit button isn't available go back to the main menu using below steps
            back_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss')
            back_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar--confirm-''dialog span')
            discard_button.click()
            print("Complex application, skipped.")

    except NoSuchElementException:
        print("No application button, skipped.")
        pass

driver.quit()


# ---------- APPLYING ONE JOB ------------
# first_job = driver.find_element(By.CSS_SELECTOR, "#ember193")
# first_job.click()
# easy_apply_button = driver.find_element(By.CSS_SELECTOR, "#ember319 > span")
# easy_apply_button.click()
# next_button = driver.find_element(By.CSS_SELECTOR, "#ember554 > span")
# next_button.click()
# review_button = driver.find_element(By.CSS_SELECTOR, "#ember571 > span")
# review_button.click()
# submit_button = driver.find_element(By.CSS_SELECTOR, "#ember582 > span")
# submit_button.click()

# JUST SAVE THE JOB AND FOLLOW THE COMPANY PAGE
# first_job = driver.find_element(By.CSS_SELECTOR, "#ember193")
# first_job.click()
# save_button = driver.find_element(By.CSS_SELECTOR, "body > div.application-outlet > div.authentication-outlet >
#                                                     div.job-search-ext > div.jobs-search-two-pane__wrapper > div >
#                                                     section.jobs-search__right-rail > div > div > div:nth-child(1) >
#                                                     div > div:nth-child(1) > div > div.jobs-unified-top-card__
#                                                     content--two-pane > div:nth-child(4) > div > button >
#                                                     span:nth-child(1)")
# save_button.click()
# follow_company_button = driver.find_element(By.CSS_SELECTOR, "#ember323 > section > div.jobs-company__box >
#                                                               div.display-flex.align-items-center.mt5 >
#                                                               button > span")
# follow_company_button.click()
