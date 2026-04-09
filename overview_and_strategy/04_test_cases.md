# Test Cases

These test cases are designed based on actual system behavior and cross-service observations.

The focus is on how individual services behave, how they interact, and where the system allows invalid or inconsistent states.

---

## User Service (ReqRes)

### Positive Scenarios

TC01 - Validate GET user with valid ID → Expect consistent user structure used across system  

TC02 - Validate POST user → Expect creation but observe incomplete response structure  

---

### Negative Scenarios

TC03 - Validate POST user with invalid data types → Expect rejection but system accepts  

TC04 - Validate POST on invalid endpoint → System still processes request  

---

### Edge Cases

TC05 - Validate repeated POST requests → Multiple users created (no idempotency)  

TC06 - Validate mismatch in ID type (string vs number) → Causes inconsistency across services  

TC07 - Validate missing fields in POST → System still accepts incomplete data  

---

## Order Service (JSONPlaceholder)

### Positive Scenarios

TC08 - Validate GET order with valid ID → Expect order with userId  

---

### Negative Scenarios

TC09 - Validate order.userId without existing user → System allows orphan records  

---

### Edge Cases

TC10 - Validate multiple orders pointing to same invalid user → Amplifies inconsistency  

TC11 - Validate large or invalid userId values → No validation enforced  

TC12 - Validate system assumes userId is always valid → Dependency not verified  

---

## GraphQL Service (Geo)

### Positive Scenarios

TC13 - Validate country query → Data returned and used directly  

---

### Negative Scenarios

TC14 - Validate invalid query → Proper error response  

---

### Edge Cases

TC15 - Validate missing or partial country data → No fallback handling  

TC16 - Validate over-fetching unnecessary data → No restriction  

TC17 - Validate dependency on external service → System fails if unavailable  

---

## Cross-Service Interaction 

### Positive Scenarios

TC18 - Validate order.userId maps correctly to user.id → Works only when assumption holds  

---

### Negative Scenarios

TC19 - Validate mismatch between order.userId and user.id → No error, system continues  

TC20 - Validate partial success (user valid, order invalid) → No failure surfaced  

---

### Edge Cases

TC21 - Validate system behavior when user exists but mapping is incorrect → Relationship not enforced  

TC22 - Validate system with inconsistent data across services → No reconciliation  

TC23 - Validate system trusts all incoming service data → No verification  

---

## Failure and Resilience

### Negative Scenarios

TC24 - Validate delayed response (httpbin) → No retry or fallback  

TC25 - Validate partial service failure → System continues with incomplete data  

---

### Edge Cases

TC26 - Validate timeout scenarios → No graceful handling  

TC27 - Validate cascading failure (one service slow impacts flow)  

---

## Security and Validation Gaps

### Negative Scenarios

TC28 - Validate malformed payload → Accepted without strict validation  

TC29 - Validate repeated requests (abuse scenario) → No rate limiting  

---

### Edge Cases

TC30 - Validate system does not enforce authentication strictly → Open access behavior  

TC31 - Validate input manipulation → System accepts unexpected values  

---

## Limitations

Geo-based validation, VPN testing, and infrastructure-level failures were not achievable due to reliance on public APIs.

However, these are identified as high-risk areas in a real-world system.