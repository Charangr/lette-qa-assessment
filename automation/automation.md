
---

## Key Design Decisions

### Lightweight Framework
A minimal structure was chosen to prioritize **clarity and system behavior** over heavy abstraction.

### POM for UI
Separates UI logic from test logic, improving readability and maintainability.

### API Client Layer
Encapsulates API calls to avoid duplication and improve structure.

### Retry Logic
Handles transient failures, which are common in distributed systems.

### Data-Driven Testing
Ensures validation across multiple inputs instead of hardcoded values.

---

## Test Coverage

The automation covers:

- UI validation (login flow)
- API validation (user creation and retrieval)
- End-to-end flow (User → Order → Geo)
- GraphQL query validation
- Security behavior (authentication gaps)
- Data consistency validation

---

## Key Scenarios Covered

### Positive Scenarios
- Valid user creation and retrieval
- Valid order creation
- Valid GraphQL query
- Successful login flow

---

### Negative Scenarios
- Invalid or missing user references in orders
- API calls without authentication
- Invalid payloads accepted by system
- Partial failures across services

---

### Edge Cases

- Multiple orders linked to non-existing users  
- Mismatch between order.userId and user.id  
- Missing fields in request payloads  
- Repeated requests (no idempotency)  
- Large or invalid userId values  
- External dependency (GraphQL) failure  
- Slow or delayed responses (simulated via httpbin)  

These scenarios highlight how the system behaves when assumptions break.

---

## Data Validation

A separate validation script checks:

- orphan records (orders without users)
- incorrect payment values
- missing references

This is critical because:
> Distributed systems often fail silently when data is inconsistent.

---

## Security Observations

- API endpoints allow access without strict authentication  
- No enforcement of access control  
- System accepts manipulated or unexpected inputs  

These indicate potential vulnerabilities in real-world scenarios.

---

## Failure and Resilience

The system was tested under:

- delayed responses  
- partial service failures  
- inconsistent data states  

Observations:
- no retry mechanisms at system level  
- no graceful failure handling  
- system continues with invalid or incomplete data  

---

## Key Risks Identified

- Data inconsistency across services  
- Lack of validation for relationships  
- Silent failures (incorrect but accepted data)  
- Dependency on external services without fallback  
- Open access behavior (security risk)  

---

## Trade-offs

- Focus on backend and data validation over UI depth  
- Limited performance and security depth  
- No real integration layer (simulation-based testing)  

---

