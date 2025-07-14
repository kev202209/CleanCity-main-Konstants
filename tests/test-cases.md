**Project:** CleanCity: Waste Pickup Scheduler  
**Date:** 2025-06-30  
**Tested by:** The Konstants
**Submitted by**: Kelvin Muendo  
**Submission Date**: 2025-06-30

# CleanCity Test Cases

| TC ID | Feature         | Test Description                                      | Steps                                                                 | Expected Result                        | Automated |
|-------|----------------|-------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------|-----------|
| TC01  | Register       | User can register a new account                       | Go to Register, fill form, submit                                    | Registration success, redirected/login | Yes       |
| TC02  | Login          | User can log in with valid credentials                | Go to Login, fill form, submit                                       | Login success, redirected/profile      | Yes       |
| TC03  | Admin Access   | Non-admin cannot access admin page                    | Try to access /admin as non-admin                                    | Redirected to login                    | Yes       |
| TC04  | Blog           | View blog, open article, add comment                  | Go to Blog, open article, add comment                                | Comment appears                        | Yes       |
| TC05  | Blog Admin     | Non-admin cannot access blog admin                    | Try to access /blog/admin as non-admin                               | Redirected to login                    | Yes       |
| TC06  | Community      | Create post, like, comment                            | Go to Community, create post, like, add comment                      | Post/comment/like appear               | Yes       |
| TC07  | Home           | Schedule a waste pickup                               | Go to Home, fill form, submit                                        | Success message                        | Yes       |
| TC08  | Awareness      | View eco tip, quiz, infographic                       | Go to Awareness                                                      | Sections visible, quiz works           | Yes       |
| TC09  | Feedback       | Submit feedback                                       | Go to Feedback, fill form, submit                                    | Success message                        | Yes       |
| TC10  | Dashboard      | View dashboard stats (if logged in)                   | Log in, go to Dashboard                                              | Stats visible                          | Yes       |
| TC11  | Navigation     | All navbar links work                                 | Click each navbar link                                               | Correct page loads                     | Yes       |
| TC12  | Logout         | User can log out                                      | Log in, click Logout                                                 | User is logged out                     | No        |
| TC13  | Error Handling | Invalid login shows error                             | Go to Login, enter wrong credentials, submit                         | Error message shown                    | No        |
| TC14  | Accessibility  | Forms have labels and ARIA attributes                 | Inspect forms                                                        | Proper labels/ARIA present             | No        |
| TC15  | Responsiveness  | The look on the site from different devices                 | Inspect forms                                                        | Proper responsiveness on a mobile phone             | No        |

**Note:** Automated = covered by Selenium scripts in `automated_tests/`.