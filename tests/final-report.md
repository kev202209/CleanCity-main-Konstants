# CleanCity Test Execution Report

## 1. Executive Summary
Testing for CleanCity Waste Pickup Scheduler was conducted using a combination of automated Selenium scripts and manual exploratory testing. All major user flows were validated, and critical defects were addressed.

## 2. Test Execution Summary

| Test Case ID | Status    | Notes                                      |
|--------------|-----------|--------------------------------------------|
| TC01         | Passed    | Automated (register_login_test.py)         |
| TC02         | Passed    | Automated (register_login_test.py)         |
| TC03         | Passed    | Automated (register_login_test.py)         |
| TC04         | Passed    | Automated (test_blog_functionality.py)     |
| TC05         | Passed    | Automated (test_blog_functionality.py)     |
| TC06         | Passed    | Automated (test_community_feed.py)         |
| TC07         | Passed    | Automated (test_main_page.py)              |
| TC08         | Passed    | Automated (test_main_page.py)              |
| TC09         | Passed    | Automated (test_main_page.py)              |
| TC10         | Passed    | Automated (test_main_page.py)              |
| TC11         | Passed    | Automated (all scripts)                    |
| TC12         | Passed    | Manual                                     |
| TC13         | Passed    | Manual                                     |
| TC14         | Passed    | Manual (checked with browser dev tools)    |

## 3. Defect Analysis

| Defect ID | Description                        | Status   | Resolution         |
|-----------|------------------------------------|----------|--------------------|
| D01       | N/A (all critical flows passed)    | Closed   | N/A                |

## 4. Test Evidence

- **Screenshots:** See `/tests/screenshots/`
- **Automated Scripts:** See `/automated_tests/`
- **Presentation video:** Click this [Link to the video](https://drive.google.com/file/d/1UWxJ5zQPZlFhE_YzRvjiG7mQY2Pdo2U8/view?usp=sharing)


## 5. Lessons Learned

- Automated UI testing with Selenium greatly improved coverage and repeatability.
- LocalStorage-based data required clearing between test runs for consistency.
- Manual testing was still needed for accessibility and error handling.

## 6. Recommendations

- Add more negative/edge case automated tests.
- Consider adding mobile/responsive tests.
- Continue to improve accessibility.

## 7. Metrics

- **Total Test Cases:** 14
- **Automated:** 11
- **Manual:** 3
- **Pass Rate:** 100%

---

**Prepared by:** The Konstants  
**Date:** July 10, 2025