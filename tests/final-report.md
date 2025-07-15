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


| Defect ID | Date       | Feature         | Description                                      | Severity | Status | Reported By |
|-----------|------------|----------------|--------------------------------------------------|----------|--------|-------------|
| D01       | 2025-07-10 | Registration   | Email validation allows emails without domain extension | Major   | Open   | QA Team     |
| D02       | 2025-07-10 | App.js         | No error boundary/global error handler           | Major   | Open   | QA Team     |
| D03       | 2025-07-10 | All Forms      | No input sanitization (potential XSS)            | Critical    | Open   | QA Team     |
| D04       | 2025-07-10 | Accessibility  | Some forms missing ARIA attributes/labels        | Minor     | Open   | QA Team     |
| D05       | 2025-07-10 | Accessibility  | the comment like on the blog allow more likes from one user/labels        | Minor      | Open   | QA Team     |
| D06       | 2025-07-10 | Responsiveness | The site navigation bar fils the whole page on mobiles devices  | Critical   | Open   | QA Team     |


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