from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # Log in as admin
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    driver.find_element(By.ID, "login-email").send_keys("admin@cleancity.com")
    driver.find_element(By.ID, "login-password").send_keys("AdminPass123")
    driver.find_element(By.CLASS_NAME, "login-btn").click()
    time.sleep(2)

    # Go to Admin page
    driver.find_element(By.LINK_TEXT, "Admin").click()
    time.sleep(1)
    assert "Admin: Manage Requests" in driver.page_source

    # (Optional) Moderate a request (complete, miss, delete)
    # Click the first 'Delete' button if present
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    if delete_buttons:
        delete_buttons[0].click()
        time.sleep(1)
        # Accept the confirm dialog (if any)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)
        except:
            pass
        print("Admin moderation action performed.")
    else:
        print("No requests to moderate.")

finally:
    driver.quit()
