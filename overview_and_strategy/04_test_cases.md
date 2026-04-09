# Advanced Test Cases (System-Level)

This table validates system behavior across loosely connected services, focusing on data inconsistency, silent failures, and dependency risks.

---

## End-to-End User → Order → Geo Flow

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC01 | Validate user exists before order mapping | Positive | Data consistency | User service available | Fetch user and order, compare IDs | userId=1 | Order.userId matches User.id | Valid relationship check |
| TC02 | Order created with non-existing user | Negative | Orphan data | No user with ID=3 | Fetch order and validate user | userId=3 | System should detect missing user | No referential validation |
| TC03 | User created after order creation | Edge | Temporal inconsistency | Order exists first | Create order then user | same userId | Should flag mismatch | Time-based inconsistency |
| TC04 | Multiple orders mapped to invalid user | Edge | Data amplification | Invalid userId used | Create multiple orders | userId=999 | Detect pattern | Bad data scales silently |

---

## Silent Failure Detection

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC05 | API returns 200 with incorrect mapping | Negative | Silent failure | Invalid relationship exists | Validate mapping | mismatched IDs | Should not be treated as success | False positive success |
| TC06 | Partial success across services | Negative | Workflow gap | User valid, order invalid | Fetch both | N/A | Should flag inconsistency | Prevent blind continuation |
| TC07 | GraphQL returns valid but irrelevant data | Edge | Data correctness | API available | Compare geo data | wrong country | Should validate relevance | Over-trust risk |
| TC08 | Correct schema but incorrect values | Negative | Hidden defect | API returns 200 | Validate values | wrong data | Should fail validation | Schema ≠ correctness |

---

## External Dependency Behavior

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC09 | Delay in external API | Positive | Latency | Delay simulated | Call endpoint | delay=3s | Response handled | Blocking dependency |
| TC10 | External service unavailable | Negative | Dependency failure | API down | Simulate failure | N/A | Fail gracefully | No fallback |
| TC11 | Repeated calls to slow API | Edge | Performance | No caching | Repeat calls | same request | Latency increases | No caching |
| TC12 | Geo returns partial data | Edge | Incomplete dependency | Missing fields | Query data | partial response | Handle gracefully | Partial dependency risk |

---

## Data Validation

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC13 | Payment value zero or negative | Negative | Financial integrity | Dataset loaded | Validate payments | amount ≤ 0 | Flag invalid | Business logic |
| TC14 | Multiple payments per order | Edge | Duplication | Dataset loaded | Count payments | >3 payments | Flag anomaly | Retry issue |
| TC15 | Order without customer | Negative | Referential integrity | Dataset loaded | Validate mapping | missing customer | Flag issue | Orphan data |
| TC16 | Duplicate order IDs | Edge | Data duplication | Dataset loaded | Check IDs | duplicate ID | Detect duplicates | Reporting risk |
| TC17 | Missing payment for completed order | Negative | Data completeness | Dataset loaded | Validate linkage | missing payment | Flag issue | Incomplete transaction |

---

## Security and Abuse Patterns

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC18 | API access without authentication | Negative | Broken auth | No token | Call API | N/A | Should reject | Open access |
| TC19 | Replay same request | Negative | Abuse | API allows POST | Repeat request | same payload | Detect duplicates | Idempotency gap |
| TC20 | Manipulated input | Negative | Input trust | None | Send invalid values | wrong types | Reject request | No validation |
| TC21 | Large payload attack | Negative | Resource abuse | None | Send large payload | large body | Limit input | DoS risk |

---

## Failure and System Behavior

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC22 | One service fails while others succeed | Negative | Partial failure | Order fails | Trigger failure | N/A | Should not proceed silently | Broken flow |
| TC23 | Cascading delay across services | Edge | Dependency chaining | One service slow | Add delay | delay=3s | Latency increases | Chain impact |
| TC24 | Inconsistent state after retry | Edge | Data mismatch | Retry logic exists | Retry request | same input | Maintain consistency | Idempotency |
| TC25 | Timeout without retry | Negative | Resilience gap | Timeout simulated | Trigger timeout | N/A | Fail cleanly | No retry |

---

## Edge Cases (Observed Behavior)

| TC ID | Scenario | Type | Risk Focus | Preconditions | Test Steps | Test Data | Expected Result | Insight |
|------|----------|------|-----------|--------------|------------|-----------|----------------|---------|
| TC26 | String vs numeric userId mismatch | Edge | Type inconsistency | None | Use string ID | "1" vs 1 | Validate type | Mapping issue |
| TC27 | Empty response with 200 status | Edge | Silent failure | API returns empty | Validate response | empty body | Detect invalid response | False success |
| TC28 | Unexpected field in response | Edge | Schema drift | None | Validate schema | extra field | Detect deviation | Schema risk |
| TC29 | Missing required field | Negative | Data loss | None | Validate fields | missing field | Fail validation | Incomplete data |
| TC30 | Conflicting data across services | Edge | Data inconsistency | None | Compare responses | mismatch | Flag inconsistency | Cross-service issue |
| TC31 | High concurrency inconsistent reads | Edge | Race condition | Load present | Simulate concurrency | parallel calls | Maintain consistency | Race condition |
| TC32 | Order created but not retrievable | Negative | Persistence gap | API unstable | Create then fetch | orderId | Should retrieve | Data loss |
| TC33 | External API returns stale data | Edge | Data freshness | Cached response | Fetch repeatedly | outdated data | Detect inconsistency | Stale data |
| TC34 | Same userId reused in different contexts | Edge | Context leak | None | Reuse ID | same ID | Validate context | Logical flaw |

---

## Limitations

Geo-based validation, VPN testing, and infrastructure-level failures were not achievable due to reliance on public APIs.

However, these remain high-risk areas in real-world systems.