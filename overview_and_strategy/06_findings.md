# Findings Report

## Overview

The testing was conducted across multiple layers of the system, including API behavior, end-to-end flows, dataset validation, performance, and basic security checks. The goal was to understand how the system behaves when independent services interact and to identify gaps in validation, consistency, and reliability.

The findings highlight that while individual components appear functional, there are critical issues in how data is handled across the system.

---

## API Behavior Findings

The APIs function correctly for basic scenarios such as fetching valid data and returning appropriate responses for invalid requests. However, significant gaps were observed in input validation and response consistency.

The system accepts invalid payloads, incorrect data types, and incomplete requests while still returning successful responses. The POST APIs are highly permissive and allow creation of resources even when the input does not meet expected standards.

It was also observed that the response structure is inconsistent across endpoints. The GET response returns a complete user object, while the POST response returns only partial data, leading to inconsistency in API design.

Another critical issue is the absence of idempotency. Repeated requests with the same payload result in multiple records being created, which can lead to duplication and data integrity issues.

---

## Data Consistency Findings

The most critical finding is the lack of validation across services. The order service allows creation of orders for any userId without verifying whether the user exists in the user service.

This leads to situations where orders are linked to non-existent users, creating orphan or inconsistent data. Since there is no enforcement of relationships, data consistency must be validated externally.

Even when mappings appear correct for sampled data, there is no guarantee of consistency because the system does not enforce it at any level.

---

## Dataset Validation Findings

The dataset validation confirmed that the structure of the data is largely consistent, with no major issues in relationships, duplicates, or missing identifiers.

However, issues were identified in data correctness and business logic. Invalid payment values were detected, which should not occur in a valid system. Additionally, unusual payment patterns were observed where multiple payments are linked to a single order.

These findings indicate that while structural integrity exists, logical validation is missing. The system allows incorrect or unrealistic data to exist without detection.

---

## Failure Handling Findings

The system does not handle failures effectively. Instead of rejecting invalid scenarios, it continues processing and returns success responses.

This behavior results in silent failures, where incorrect data is accepted and propagated without any indication of error. Such failures are more dangerous than explicit errors because they are harder to detect and can impact downstream systems.

There is also no retry or recovery mechanism at the system level, and partial failures are not handled in a controlled manner.

---

## Security Findings

Security validation revealed that APIs can be accessed without strict authentication, and there is limited enforcement of access control.

The system accepts manipulated or unexpected inputs without validation, which increases the risk of data corruption and unauthorized operations.

These gaps indicate that security is not enforced consistently across the system.

---

## Performance Observations

Basic performance testing indicates that the system can handle requests under normal conditions. However, there is no clear handling of delays, timeouts, or high-load scenarios.

The absence of structured performance controls and monitoring makes it difficult to assess system behavior under stress.

---

## Overall Assessment

The system appears functional at a surface level but lacks strong validation, consistency enforcement, and error handling.

A key observation is that the system prioritizes availability over correctness. It continues to process requests even when the data is invalid or inconsistent.

This leads to a critical risk where the system may produce incorrect results while appearing to work correctly.

---

## Conclusion

The findings demonstrate that validating a distributed system requires more than checking individual components. It requires verifying how data flows across services and ensuring that relationships, constraints, and validations are properly enforced.

The current system lacks these controls, making it prone to data inconsistencies, silent failures, and reliability issues.

This highlights the importance of enforcing validation, ensuring consistency, and designing systems that fail explicitly when incorrect conditions are encountered.