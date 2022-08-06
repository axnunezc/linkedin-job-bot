from selenium import webdriver
from decouple import config
import time
from selenium.common.exceptions import NoSuchElementException

email = "axelbirthdaywisher@gmail.com"
password = config("PASSWORD")
phone_num = config("PHONE")

chrome_driver_path = "/Users/axel/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open linkedin
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20developer")

# Redirect to Sign In page
driver.find_element_by_class_name("nav__button-secondary").click()

time.sleep(2)

# Enter email
email_input = driver.find_element_by_id("username")
email_input.send_keys(email)

# Enter password
password_input = driver.find_element_by_id("password")
password_input.send_keys(password)

# Click on Sign In Button
driver.find_element_by_class_name("btn__primary--large").click()

# Search for first available job posting
job_postings = driver.find_elements_by_class_name("job-card-container--clickable")

for posting in job_postings:
# Redirect to Job Application page
    time.sleep(4)
    posting.click()
    time.sleep(2)
    
    try:
        apply_btn = driver.find_element_by_class_name("jobs-apply-button")
        
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

    else: 
        apply_btn.click()
        
        # Enter phone number
        phone_input = driver.find_element_by_class_name("fb-single-line-text__input")
        phone_input.send_keys(phone_num)

        # Submit application if only requires phone number
        footer_btn = driver.find_element_by_css_selector("footer button")
        if footer_btn.get_attribute("aria-label") == "Submit application":
            footer_btn.click()
            driver.find_element_by_class_name("artdeco-modal__dismiss").click()
        else:
            driver.find_element_by_class_name("artdeco-modal__dismiss").click()
            driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1].click()
            time.sleep(2)
            driver.find_element_by_class_name("artdeco-toast-item__dismiss").click()
            

