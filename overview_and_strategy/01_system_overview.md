# System Overview

This project tests a distributed system where multiple services operate independently. The focus is to understand how data moves across services and where inconsistencies or failures can occur.

The system includes a User Service, an Order Service, and a Geo Service. Each service works separately and communicates only through API calls. There is no shared database or validation layer between them.

The flow starts with fetching a user, followed by retrieving or creating an order that contains a userId. This userId is then matched with the user data, and additional country information is fetched from the Geo Service. The final step is to validate whether the data is consistent across all services.

Since the services are not integrated, the system depends on assumptions that the data is valid. There is no mechanism to enforce correctness across services.

---

## Architecture

The system follows a distributed architecture where each service is independent and loosely coupled. Data flows between services through API calls without any central validation.

The Order Service references users through userId, but this relationship is not enforced. The Geo Service provides additional data without validating the source.

There is no coordination between services, and failures in one service are not handled by others. This creates a system that is simple but prone to inconsistency and invalid states.

