# QA + AI Distributed System Testing

## Overview

This project focuses on testing a distributed system by combining API testing, UI validation, data validation, and performance analysis. The objective is to understand how independent services behave together, identify inconsistencies, and validate system behavior under realistic scenarios.

The approach is not limited to verifying functionality. It focuses on how data flows across services, how failures are handled, and whether the system maintains correctness.

---

## Project Structure

LetteAi_assessment/
├── API_manualTesting/
│ ├── API_ManualSimulation.md
│ └── evidence/
│
├── automation/
│ ├── clients/
│ ├── pages/
│ ├── tests/
│ ├── utils/
│ ├── config.py
│ ├── validate_data.py
│ └── test_data.json
│
├── dataset_validation/
│ ├── datasetValidation.md
│ ├── validate_dataset.py
│ └── datasets (customers, orders, payments)
│
├── overview_and_strategy/
│ ├── system overview
│ ├── test strategy
│ ├── test cases
│ ├── bug reports
│ └── findings
│
└── perfomance_test/
├── performance_report.md
└── performance_test.js


The `API_manualTesting` folder contains the manual API simulation and supporting evidence used to validate system behavior before automation.

The `automation` module contains the test framework implemented using Python and pytest. It includes API tests, UI tests, end-to-end scenarios, security checks, and supporting utilities.

The `dataset_validation` section focuses on validating data integrity across datasets, including both the validation logic and the datasets used.

The `overview_and_strategy` folder provides the overall understanding of the system, including the test strategy, detailed test cases, identified bugs, and key findings.

The `perfomance_test` folder contains performance testing scripts and the corresponding analysis report.


## Deliverables

This project includes all key deliverables expected for validating a distributed system, covering strategy, execution, and analysis.

### Test Strategy

A risk-based testing approach is defined to focus on the most critical areas such as data consistency, service interaction, and failure handling. The strategy explains trade-offs made during testing and defines the overall coverage across UI, APIs, data, and performance.

Location:  
./overview_and_strategy/03_test_strategy.md  

---

### Test Cases

A comprehensive set of test cases is designed to validate system behavior under different conditions. This includes normal scenarios where the system is expected to work correctly, failure scenarios to test robustness, and edge cases to simulate real-world unpredictability.

Location:  
./overview_and_strategy/04_test_cases.md  

---

### Bug Reports

Detailed bug reports are documented with clear explanations of issues, along with their severity and impact. Each bug is supported with observations, logs, or payload-level evidence to justify its classification.

Location:  
./overview_and_strategy/05_bug_reports.md  

---

### Automation Framework

A lightweight and scalable automation framework is implemented using Python and pytest. It validates API behavior, UI flows, end-to-end scenarios, and basic security checks, ensuring repeatable and reliable testing.

Location:  
./automation/  

---

### Data Validation Script

A Python-based validation script is used to verify dataset integrity across customers, orders, and payments. It checks relationships, detects inconsistencies, and ensures the data aligns with expected business logic.

Location:  
./dataset_validation/validate_dataset.py  

---

### Performance Report

Performance testing is conducted to analyze how the system behaves under load and delay conditions. The report highlights response behavior, potential bottlenecks, and system limitations.

Location:  
./perfomance_test/performance_report.md  

---

### Security Findings

Security-related observations are identified during testing, including gaps in authentication, input validation, and access control. The impact of these issues on system reliability is also explained.

Location:  
./automation/tests/test_security.py  
./overview_and_strategy/06_findings.md  

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