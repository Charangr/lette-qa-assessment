# Advanced Test Cases (System-Level)

## End-to-End User → Order → Geo Flow

| TC ID | Scenario | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|-----------|--------------|------------|-----------|----------------|---------|
| TC01 | Validate user exists before order mapping | Data consistency | User service available | 1. Fetch user 2. Fetch order 3. Compare IDs | userId=1 | Order.userId matches User.id | Ensures system does not assume valid relationships |
| TC02 | Order created with non-existing user | Orphan data | No user with ID=3 | 1. Fetch order with userId=3 2. Validate user | userId=3 | System should detect missing user | Identifies lack of referential validation |
| TC03 | User created after order creation | Temporal inconsistency | Order exists first | 1. Create order 2. Create user later | same userId | System should reconcile or flag mismatch | Checks time-based data integrity issues |
| TC04 | Multiple orders mapped to invalid user | Data amplification risk | Invalid userId used | 1. Create multiple orders with invalid userId | userId=999 | System should detect pattern | Highlights how bad data scales silently |

---

## Silent Failure Detection

| TC ID | Scenario | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|-----------|--------------|------------|-----------|----------------|---------|
| TC05 | API returns 200 with incorrect mapping | Silent failure | Invalid relationship exists | 1. Fetch order 2. Validate user mapping | mismatched IDs | System should not treat as success | Detects false positives in API success |
| TC06 | Partial success across services | Incomplete workflow | User valid, order invalid | 1. Fetch user 2. Fetch invalid order | N/A | System should flag incomplete state | Ensures system does not proceed blindly |
| TC07 | GraphQL returns valid response but irrelevant data | Data correctness | API available | 1. Query country 2. Compare with user context | country mismatch | System should validate relevance | Detects over-trust in external APIs |

---

## External Dependency Behavior

| TC ID | Scenario | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|-----------|--------------|------------|-----------|----------------|---------|
| TC08 | Delay in external API (Geo service) | Latency impact | API delay simulated | 1. Call delayed endpoint 2. Observe system flow | delay=3s | System should handle delay gracefully | Identifies blocking dependency issues |
| TC09 | External service unavailable | Dependency failure | API down | 1. Simulate failure 2. Trigger workflow | N/A | System should fail gracefully | Checks resilience strategy |
| TC10 | Repeated calls to slow API | Performance degradation | No caching | 1. Trigger repeated calls | same request | Response time increases | Highlights absence of caching |

---

## Data Validation (Dataset-Level Thinking)

| TC ID | Scenario | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|-----------|--------------|------------|-----------|----------------|---------|
| TC11 | Payment value is zero or negative | Financial integrity | Dataset loaded | 1. Validate payment values | amount ≤ 0 | Records should be flagged invalid | Ensures business logic validation |
| TC12 | Multiple payments for single order | Duplicate / retry issue | Dataset loaded | 1. Count payments per order | >3 payments | System should flag anomaly | Detects retry or duplication issues |
| TC13 | Order exists without customer | Referential integrity | Dataset loaded | 1. Validate order.customerId | missing customer | Should be flagged | Identifies orphan records |

---

## Security and Abuse Patterns

| TC ID | Scenario | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|-----------|--------------|------------|-----------|----------------|---------|
| TC14 | Access API without authentication | Broken auth | No token | 1. Call API without token | N/A | Should be rejected | Detects open access risk |
| TC15 | Replay same request multiple times | Abuse / duplication | API accepts requests | 1. Send same POST repeatedly | same payload | System should detect duplicates | Tests idempotency gap |
| TC16 | Manipulated input across services | Input trust issue | None | 1. Send unexpected values | invalid types | Should be rejected | Checks lack of validation |

---

## Failure and System Behavior

| TC ID | Scenario | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|-----------|--------------|------------|-----------|----------------|---------|
| TC17 | One service fails while others succeed | Partial failure | Order fails, user works | 1. Trigger failure 2. Observe flow | N/A | System should not proceed silently | Detects workflow inconsistency |
| TC18 | Cascading delay across services | System slowdown | One service slow | 1. Add delay 2. Trigger full flow | delay=3s | Overall response increases | Identifies dependency chaining |
| TC19 | Inconsistent state across retries | Data mismatch | Retry logic exists | 1. Trigger retry scenario | same request | Data should remain consistent | Checks idempotency and stability |

## Limitations

Geo-based validation, VPN testing, and infrastructure-level failures were not achievable due to reliance on public APIs.

However, these are identified as high-risk areas in a real-world system.

