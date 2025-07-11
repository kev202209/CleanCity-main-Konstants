from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # Go to Community page
    driver.find_element(By.LINK_TEXT, "Community").click()
    time.sleep(1)
    assert "Community Feed" in driver.page_source

    # Create a new post
    textarea = driver.find_element(By.XPATH, "//textarea[@placeholder='Share something with the community...']")
    textarea.send_keys("This is a Selenium community test post.")
    driver.find_element(By.XPATH, "//button[text()='Post']").click()
    time.sleep(1)
    assert "This is a Selenium community test post." in driver.page_source

    # Like the first post
    like_buttons = driver.find_elements(By.CLASS_NAME, "like-btn")
    assert like_buttons, "No like buttons found"
    like_buttons[0].click()
    time.sleep(1)

    # Open comments for the first post
    comment_buttons = driver.find_elements(By.CLASS_NAME, "comment-btn")
    assert comment_buttons, "No comment buttons found"
    comment_buttons[0].click()
    time.sleep(1)

    # Add a comment to the first post
    comment_inputs = driver.find_elements(By.XPATH, "//input[@placeholder='Add a comment...']")
    assert comment_inputs, "No comment input found"
    comment_inputs[0].send_keys("This is a Selenium test comment on community post.")
    comment_forms = driver.find_elements(By.XPATH, "//button[text()='Comment']")
    assert comment_forms, "No comment submit button found"
    comment_forms[0].click()
    time.sleep(1)
    assert "This is a Selenium test comment on community post." in driver.page_source

    print("Community feed test completed successfully.")

finally:
    driver.quit()