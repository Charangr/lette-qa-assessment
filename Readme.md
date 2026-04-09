# QA + AI Distributed System Testing

## Overview

This project focuses on testing a distributed system by combining API testing, UI validation, data validation, and performance analysis. The objective is to understand how independent services behave together, identify inconsistencies, and validate system behavior under realistic scenarios.

The approach is not limited to verifying functionality. It focuses on how data flows across services, how failures are handled, and whether the system maintains correctness.

---

## Project Structure

The project is organized into separate modules, each focusing on a specific area of testing.

The API_manualTesting section contains the manual API simulation along with supporting evidence used to validate system behavior before automation.  
[View Manual Testing](./API_manualTesting/API_ManualSimulation.md)

The automation module contains the test framework implemented using Python and pytest. It includes API tests, UI tests, end-to-end scenarios, and security validations.  
[View Automation](./automation/)

The dataset_validation section focuses on validating data integrity across customers, orders, and payments using datasets and a Python validation script.  
[View Dataset Validation](./dataset_validation/datasetValidation.md)

The overview_and_strategy section provides the system understanding, test strategy, detailed test cases, bug reports, and final findings.  
[View Strategy and Findings](./overview_and_strategy/01_system_overview.md)

The performance_test section contains performance testing scripts and the corresponding analysis report.  
[View Performance Report](./perfomance_test/performance_report.md)

## Deliverables

## Deliverables

All required deliverables are implemented and organized for easy access.

### Test Strategy  
A risk-based testing approach covering trade-offs, assumptions, and system behavior.  
[Open Test Strategy](./overview_and_strategy/03_test_strategy.md)

---

### Test Cases  
Includes positive, negative, and edge case scenarios validating system behavior.  
[Open Test Cases](./overview_and_strategy/04_test_cases.md)

---

### Bug Reports  
Contains identified issues with severity, priority, and supporting evidence.  
[Open Bug Reports](./overview_and_strategy/05_bug_reports.md)

---

### Automation Framework  
A Python-based framework covering API, UI, end-to-end, and security testing.  
[Open Automation Module](./automation/)

---

### Data Validation Script  
Validates dataset integrity and identifies inconsistencies in data relationships.  
[Open Validation Script](./dataset_validation/validate_dataset.py)

---

### Performance Report  
Analyzes system behavior under load and highlights bottlenecks.  
[Open Performance Report](./perfomance_test/performance_report.md)

---

### Security Findings  
Highlights vulnerabilities and their impact on system reliability.  
[Open Security Tests](./automation/tests/test_security.py)  
[Open Findings](./overview_and_strategy/06_findings.md)
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