# CleanCity QA Test Plan

**Date:** 2025-06-30  
**Tested by:** The Konstants
**Submitted by**: Kelvin Muendo  
**Submission Date**: 2025-07-08

## 1. Introduction
This document outlines the test strategy, objectives, scope, and approach for the CleanCity Waste Pickup Scheduler project.

## 2. Objectives
- Ensure all major user flows work as intended (registration, login, scheduling, feedback, blog, community, admin).
- Validate UI/UX consistency and accessibility.
- Detect and document defects early.

## 3. Scope
### In Scope
- Functional testing of all user-facing features.
- Automated UI testing (Selenium).
- Manual exploratory testing.
- Cross-browser compatibility (Chrome, Firefox).

### Out of Scope
- Mobile device testing (unless specified).
- Performance/load testing.

## 4. Test Strategy
- **Automated Testing:** Selenium scripts for core flows (register, login, blog, community, main pages).
- **Manual Testing:** Exploratory and edge-case validation.
- **Regression Testing:** Rerun automated scripts after each major change.

## 5. Test Environment
- Localhost: http://localhost:3000
- Browsers: Chrome (primary), Firefox (secondary)
- Data: LocalStorage-based, reset before each test run

## 6. Test Deliverables
- Test cases and checklists (`test-cases.md`)
- Automated test scripts (Selenium)
- Defect log
- Test execution report

## 7. Roles & Responsibilities
- Test Lead: Kelvin Muendo
- Testers: Kelvin Muendo, Efi Susana, Suliat Said
- Automation: Efi Susana, Kelvin Muendo
- Documentation: Sulait Said, Efi Susana

## 8. Risks & Mitigation
- **Risk:** LocalStorage data persistence may affect test repeatability.
  - **Mitigation:** Clear LocalStorage before each test.
- **Risk:** Incomplete test coverage for admin-only features.
  - **Mitigation:** Use test admin accounts for full coverage.
