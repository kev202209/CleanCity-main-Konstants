from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # 1. Check brand
    brand = driver.find_element(By.CLASS_NAME, "navbar-brand")
    assert "CleanCity" in brand.text

    # 2. Go to Register page
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(1)
    assert "Sign Up" in driver.page_source

    # Fill and submit register form
    driver.find_element(By.ID, "register-name").send_keys("Test User")
    driver.find_element(By.ID, "register-email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "register-password").send_keys("testpass123")
    driver.find_element(By.CLASS_NAME, "register-btn").click()
    time.sleep(1)

    # 3. Go to Login page
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    assert "Sign In" in driver.page_source

    # Fill and submit login form
    driver.find_element(By.ID, "login-email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "login-password").send_keys("testpass123")
    driver.find_element(By.CLASS_NAME, "login-btn").click()
    time.sleep(2)

    # 4. Try to access Admin page (should redirect to Login if not admin)
    driver.find_element(By.LINK_TEXT, "Admin").click()
    time.sleep(1)
    if "Sign In" in driver.page_source or "Login" in driver.page_source:
        print("Redirected to Login as expected for Admin page.")
    else:
        # If admin, check for admin dashboard
        assert "Admin: Manage Requests" in driver.page_source
        print("Admin dashboard loaded.")

    print("Test completed successfully.")

finally:
    driver.quit()