# Test Strategy

## Approach

The testing approach started with understanding the system as a distributed setup rather than independent APIs. Since services are not integrated, the focus was on how data flows across them and where this flow can break. The goal was to validate system behavior under real conditions, not just expected outputs.

---

## Testing Flow

The testing followed a simple flow to reflect real usage:

1. Validate individual APIs to understand basic behavior  
2. Introduce negative and edge cases to identify weaknesses  
3. Combine services into an end-to-end flow (User → Order → Geo)  
4. Validate data consistency across services  
5. Introduce failures and observe system behavior  

This flow ensures that testing moves from isolated validation to system-level understanding.

---

## Key Decisions

The primary decision was to prioritize data consistency over isolated API validation. The system depends on userId relationships that are not enforced, making data integrity the highest risk.

End-to-end testing was preferred because testing services in isolation does not reveal cross-service issues.

---

## Assumptions

| Assumption | Reason | Validation Approach |
|-----------|--------|-------------------|
| APIs behave as documented | Public APIs are used as system base | Verified through functional testing |
| Responses are structurally correct | Required for flow to work | Schema and field checks |
| userId represents valid user | Core dependency between services | Cross-service validation |
| Services operate independently | No integration layer exists | Observed through testing |

---

## Rules Followed

- Testing is not limited to happy paths  
- Negative and edge cases are included in every step  
- A successful response is validated for correctness  
- Cross-service validation is mandatory  

---

## Risk-Based Prioritization

Data consistency is treated as the highest risk because incorrect relationships can break the system. API validation and edge cases follow next. Failure scenarios are included to understand behavior under stress. Performance, security, and UI testing are explored at a high level.

---

## Trade-offs

- Focus on backend behavior over UI testing  
- Depth in core areas instead of full coverage  
- Performance and security tested at a surface level  

---

## Limitations

- No real integration between services  
- Consistency validation is external  
- Limited real-world constraints such as authentication and persistence  

---

## Key Risks Identified

- Orders can exist without valid users  
- System accepts invalid data without validation  
- Silent failures where incorrect data is returned  
- No mechanism to enforce consistency  

---

## Justification

This strategy focuses on identifying system weaknesses rather than verifying expected functionality. Decisions are based on risk, with priority given to scenarios that can lead to incorrect system behavior. The approach reflects real-world conditions where data may be invalid, incomplete, or inconsistent.