from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # Go to Blog page
    driver.find_element(By.LINK_TEXT, "Blog").click()
    time.sleep(1)
    assert "CleanCity Blog" in driver.page_source

    # Check for featured posts
    assert "Featured Posts" in driver.page_source

    # Open the first featured article
    featured_links = driver.find_elements(By.LINK_TEXT, "Read More")
    assert featured_links, "No featured articles found"
    featured_links[0].click()
    time.sleep(1)

    # Check article content
    assert "Comments" in driver.page_source

    # Add a comment
    comment_input = driver.find_element(By.XPATH, "//input[@placeholder='Add a comment...']")
    comment_input.send_keys("This is a Selenium test comment.")
    driver.find_element(By.XPATH, "//button[text()='Post']").click()
    time.sleep(1)
    assert "This is a Selenium test comment." in driver.page_source

    # Go back to Blog page
    driver.find_element(By.LINK_TEXT, "← Back to Blog").click()
    time.sleep(1)

    # Try to access Blog Admin (should redirect to login if not admin)
    driver.get("http://localhost:3000/blog/admin")
    time.sleep(1)
    if "Sign In" in driver.page_source or "Login" in driver.page_source:
        print("Redirected to Login as expected for Blog Admin page.")
    else:
        # If admin, try to create a new post
        driver.find_element(By.XPATH, "//input[@placeholder='Title']").send_keys("Selenium Test Post")
        driver.find_element(By.XPATH, "//textarea").send_keys("This is a test post created by Selenium.")
        driver.find_element(By.XPATH, "//input[@placeholder='Tags (comma separated)']").send_keys("Test, Selenium")
        driver.find_element(By.XPATH, "//button[contains(text(),'Create')]").click()
        time.sleep(1)
        assert "Selenium Test Post" in driver.page_source
        print("Blog post created as admin.")

    print("Blog functionality test completed successfully.")

finally:
    driver.quit()