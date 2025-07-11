from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# This test assumes you have a user that can log in and that NotificationBell uses localStorage

def add_notification(driver, text="Test notification"):
    # Add a notification to localStorage via JS
    script = '''
    let notifications = JSON.parse(localStorage.getItem('ccNotifications') || '[]');
    notifications.push({text: arguments[0], time: new Date().toLocaleString(), read: false});
    localStorage.setItem('ccNotifications', JSON.stringify(notifications));
    '''
    driver.execute_script(script, text)


driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # Log in (assumes test user exists)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    driver.find_element(By.ID, "login-email").send_keys("user1@test.com")
    driver.find_element(By.ID, "login-password").send_keys("TestPass123")
    driver.find_element(By.CLASS_NAME, "login-btn").click()
    time.sleep(2)

    # Add a notification
    add_notification(driver, "Selenium notification test")
    driver.refresh()
    time.sleep(1)

    # Check NotificationBell unread count
    bell = driver.find_element(By.CLASS_NAME, "notification-button")
    badge = driver.find_element(By.CLASS_NAME, "notification-badge")
    assert badge.text == "1"
    bell.click()
    time.sleep(1)
    assert "Selenium notification test" in driver.page_source

    # Clear all notifications
    clear_btn = driver.find_element(By.XPATH, "//button[text()='Clear All']")
    clear_btn.click()
    time.sleep(1)
    assert "No notifications" in driver.page_source
    print("NotificationBell test completed successfully.")

finally:
    driver.quit()
