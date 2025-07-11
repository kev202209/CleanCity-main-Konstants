# CleanCity Edge Case & Negative Test Scenarios

| Scenario ID | Feature         | Description                                      | Steps                                                                 | Expected Result                        |
|-------------|----------------|--------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------|
| EC01        | Registration   | Register with very long name/email                | Enter >50 chars in name, >100 in email, submit                        | Error shown, input rejected            |
| EC02        | Registration   | Register with invalid email (no @, no domain)     | Enter 'user', 'user@', 'user@site' as email, submit                   | Error shown, input rejected            |
| EC03        | Login          | Login with wrong password                         | Enter valid email, wrong password, submit                              | Error shown, login fails               |
| EC04        | Home           | Schedule pickup with missing required fields      | Leave fields blank, submit                                            | Error shown, input rejected            |
| EC05        | Feedback       | Submit feedback with empty fields                 | Leave fields blank, submit                                            | Error shown, input rejected            |
| EC06        | Blog/Community | Enter XSS payload in comment/post                 | Enter <script>alert(1)</script> in comment/post, submit               | Input sanitized, no script executed    |
| EC07        | All Forms      | Enter unicode/international characters            | Enter unicode in all text fields, submit                              | Accepted, displayed correctly          |
| EC08        | All Forms      | Enter only whitespace in required fields          | Enter spaces/tabs, submit                                             | Error shown, input rejected            |
