from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # Log in as a user
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    driver.find_element(By.ID, "login-email").send_keys("user1@test.com")
    driver.find_element(By.ID, "login-password").send_keys("TestPass123")
    driver.find_element(By.CLASS_NAME, "login-btn").click()
    time.sleep(2)

    # Go to Profile page
    driver.find_element(By.LINK_TEXT, "Profile").click()
    time.sleep(1)
    assert "Profile" in driver.page_source or "profile" in driver.current_url
    print("Profile page loaded.")

    # (Optional) Edit profile fields if available
    # Add steps here if your profile page supports editing

finally:
    driver.quit()
