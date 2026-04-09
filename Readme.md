# QA  Distributed System Testing

A brief overview of the architecture, along with a concise demonstration of the work and key scripts :-(https://drive.google.com/file/d/1l9TlQVqkV45M9EXCtrC7dnVlIxBROuG6/view?usp=sharing)

## Overview

This project focuses on testing a distributed system by combining API testing, UI validation, data validation, and performance analysis. The objective is to understand how independent services behave together, identify inconsistencies, and validate system behavior under realistic scenarios.

The approach is not limited to verifying functionality. It focuses on how data flows across services, how failures are handled, and whether the system maintains correctness.

---

## Project Structure

The project is organized into dedicated modules, each representing a specific stage of testing and analysis.

The API_manualTesting section contains the manual API exploration performed using Postman. It includes simulation of real-world flows, validation of assumptions, screenshots, and JSON evidence used to identify inconsistencies before automation was introduced.  
[Open Folder](./API_manualTesting/)

The automation module contains the complete test framework implemented using Python and pytest. It includes API testing, UI validation, end-to-end flow checks, GraphQL validation, and security-related test scenarios along with reusable clients, utilities, and configuration.  
[Open Folder](./automation/)

The dataset_validation section focuses on validating data integrity across customers, orders, and payments. It includes datasets and a Python script used to detect inconsistencies, orphan records, and logical issues in the data.  
[Open Folder](./dataset_validation/)

The overview_and_strategy section provides the full understanding of the system along with the testing approach. It includes system overview, test strategy, detailed test cases, bug reports, and final findings derived from the testing process.  
[Open Folder](./overview_and_strategy/)

The performance_test section contains performance testing scripts and analysis of system behavior under load and delay conditions.  
[Open Folder](./perfomance_test/)


## Deliverables

All deliverables are implemented with a focus on system behavior, data consistency, and real-world validation.

### System Architecture (High-Level)

A high-level understanding of how the system is structured and how services interact logically, including assumptions made for distributed behavior.  
[View Architecture](./overview_and_strategy/01_system_overview.md)

---

### Test Strategy

A risk-based testing approach that focuses on data consistency, service interaction, and failure scenarios. It also explains trade-offs, assumptions, and coverage decisions made during testing.  
[View Strategy](./overview_and_strategy/03_test_strategy.md)

---

### Test Cases

Detailed test cases covering API, end-to-end flows, GraphQL validation, and system-level scenarios. These include positive, negative, and edge case validations.  
[View Test Cases](./overview_and_strategy/04_test_cases.md)

---

### Bug Reports

Documented issues identified during testing with clear reasoning, severity classification, and supporting observations.  
[View Bug Reports](./overview_and_strategy/05_bug_reports.md)

---

### Automation Framework

A Python-based framework designed to validate system behavior across multiple layers including APIs, UI, and end-to-end flows. It uses reusable clients, structured test cases, and utilities to ensure scalability and clarity.  
[Open Framework](./automation/)

---

### Key Scripts

Important scripts used across the project for validation and execution.

The dataset validation script verifies relationships and detects inconsistencies in structured data.  
[View Script](./dataset_validation/validate_dataset.py)

The API client layer handles request abstraction and simplifies interaction with services.  
[View Client](./automation/clients/)

---

### Performance Testing

Performance testing is implemented using a script that simulates load and measures response behavior under delay conditions. The analysis highlights system limitations and response patterns.  
[View Script](./perfomance_test/performance_test.js)  
[View Report](./perfomance_test/performance_report.md)

---

### Security Findings

Security gaps identified during testing, including missing validation, weak input handling, and lack of access control, are documented as part of the overall findings.  
[View Security Tests](./automation/tests/test_security.py)  
[View Findings](./overview_and_strategy/06_findings.md)
---
## Observability and Debugging

I didn’t rely on logs alone because in this setup logs are either limited or not trustworthy. I treated the API responses themselves as the source of truth and traced the flow step by step.

### If logs were missing, how would you proceed?

If logs are missing, I don’t get blocked. I recreate the flow and observe inputs and outputs at each step. I compare what I send versus what I get back, and more importantly, whether the data still makes sense across services.  

If something breaks, I isolate the step. If user is correct but order is wrong, the problem is in mapping. If both are correct but final output is wrong, then it’s integration logic. Basically, I narrow it down instead of guessing.

---

### How did you debug failures in this setup?

I didn’t debug blindly. I followed the flow.

First I validated the user. Then I checked how the order is created. Then I mapped userId with user.id. Wherever the mismatch happens, that’s the failure point.

Most issues here were not technical failures but logical ones. The system was accepting bad data and still saying “success”, which is actually more dangerous.

---

## Production Scenario

If I have 30 minutes before release, I don’t try to test everything. I go straight to what can break the system badly.

I check core flows like user creation, order mapping, and whether invalid data is being accepted. If the system is returning success with wrong data, that’s a red flag immediately.

---

### What is your go or no-go decision based on?

My decision is simple.  

If the system is working but producing incorrect data, it’s a no-go.  

If everything is correct for core flows and issues are minor or cosmetic, it’s a go.

I care more about correctness than just “it works”.

---

### What risks are you willing to accept?

I can accept small UI issues or minor delays because they don’t break the system.

But I won’t accept anything related to data inconsistency, missing validation, or duplicate data creation. Those are silent issues and much harder to fix later.

---


## Questions and Answers

### What are the key risks in this system?

The main risk is data inconsistency across services. Since services are not integrated, there is no validation of relationships such as orders linked to valid users. The system accepts incorrect data while still returning success responses, which can lead to silent failures and unreliable outcomes.

---

### Why is this considered a serious issue?

The system does not fail when it should. Instead of rejecting invalid inputs or broken relationships, it continues processing. This makes issues harder to detect because everything appears to work while underlying data is incorrect.

---

### What trade-offs were made during testing?

The focus was placed on backend, data validation, and system-level behavior rather than deep UI testing. Performance and security testing were explored at a basic level instead of full-depth analysis. The goal was to prioritize areas with the highest risk in distributed systems.

---

### Why was a simulation approach used instead of real integration?

The services used are independent and not actually connected. To reflect real-world behavior, the system was treated as if it were integrated, and consistency was validated manually. This approach helps uncover logical issues even when technical integration is missing.

---

### What are the limitations of this project?

The system is tested using public APIs, so there is no control over backend logic or enforcement of constraints. Performance testing is limited to basic scenarios and does not represent full production load. Security testing focuses on identifying gaps rather than performing deep penetration testing.

---

### What does this project demonstrate?

It demonstrates how a distributed system can appear functional while still producing incorrect data. It highlights the importance of validating relationships, enforcing constraints, and not relying solely on API success responses.

---

## Tools Used

Testing and validation were performed using Postman for manual API exploration, Python with pytest and requests for automation, and public APIs such as ReqRes, JSONPlaceholder, and GraphQL endpoints. Dataset validation was performed using Python scripts, and performance testing was conducted using k6.

---

## Author

Charan G R  
MSc Computing (Data Analytics), Dublin City University  

---
