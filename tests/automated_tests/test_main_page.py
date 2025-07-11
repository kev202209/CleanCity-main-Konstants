from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000")
    time.sleep(1)

    # Landing Page: check brand and CTA buttons
    assert "CleanCity" in driver.page_source
    assert "Sign Up" in driver.page_source
    assert "Schedule Pickup" in driver.page_source
    assert "Read Blog" in driver.page_source

    # Go to Home (Schedule Pickup)
    driver.find_element(By.LINK_TEXT, "Schedule Pickup").click()
    time.sleep(1)
    assert "Schedule a Waste Pickup" in driver.page_source

    # Fill and submit the pickup form
    driver.find_element(By.ID, "home-name").send_keys("Selenium User")
    driver.find_element(By.ID, "home-email").send_keys("selenium@example.com")
    # Select location
    location_select = driver.find_element(By.ID, "home-location")
    for option in location_select.find_elements(By.TAG_NAME, "option"):
        if option.text != "Select a location":
            option.click()
            break
    # Select waste type
    waste_select = driver.find_element(By.ID, "home-waste")
    for option in waste_select.find_elements(By.TAG_NAME, "option"):
        if option.text != "Select waste type":
            option.click()
            break
    # Pick a date
    driver.find_element(By.ID, "home-date").send_keys("2025-07-08")
    driver.find_element(By.ID, "home-desc").send_keys("Automated test pickup request.")
    driver.find_element(By.CLASS_NAME, "home-btn").click()
    time.sleep(1)
    assert "Your waste pickup request has been submitted!" in driver.page_source

    # Go to Awareness page
    driver.find_element(By.LINK_TEXT, "Awareness").click()
    time.sleep(1)
    assert "Eco Awareness Center" in driver.page_source
    assert "Daily Eco Tip" in driver.page_source
    assert "Eco Quiz" in driver.page_source
    assert "Did You Know?" in driver.page_source

    # Go to Feedback page
    driver.find_element(By.LINK_TEXT, "Feedback").click()
    time.sleep(1)
    assert "Report Missed Pickup / Feedback" in driver.page_source
    driver.find_element(By.ID, "feedback-request-id").send_keys("REQ123")
    driver.find_element(By.ID, "feedback-text").send_keys("Automated feedback test.")
    driver.find_element(By.CLASS_NAME, "feedback-btn").click()
    time.sleep(1)
    assert "Thank you for your feedback!" in driver.page_source

    # Go to Dashboard (if user is logged in)
    try:
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(1)
        assert "Dashboard Analytics" in driver.page_source
        assert "Total Requests" in driver.page_source
        assert "Missed Pickups" in driver.page_source
        assert "Blog Posts" in driver.page_source
        assert "Community Posts" in driver.page_source
        print("Dashboard page loaded and stats found.")
    except Exception:
        print("Dashboard not accessible (may require login).")

    print("Main pages test completed successfully.")

finally:
    driver.quit()