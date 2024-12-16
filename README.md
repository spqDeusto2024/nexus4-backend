# Nexus4

## Introduction

Nexus4 is a project designed for the management of a nuclear shelter.

### Main Features:
- **Management of the shelter's tenants and their families**
- **Management of the shelter's resources**
- **Management of the shelter's alarms**
- **Management of the shelter's rooms**

---

## Execution

To execute this project, you need to have the following installed:

- **Docker Desktop**
- **WSL2** (Windows Subsystem for Linux 2)
- **Node.js**

### Steps to Run the Project:

1. **Clone the repositories** `nexus4-backend` and `nexus4-frontend` to your WSL2 machine.
2. Open a terminal and navigate to the root of the project `nexus4-backend`.
3. Run the following command to build the backend:

   ```bash
   ./build.sh
   ```

4. Once the build is complete, run the following command to start the backend services:

   ```bash
   docker-compose up
   ```

5. Open a **new terminal** and navigate to the root of the project `nexus4-frontend`.
6. Run the following command to build and start the frontend:

   ```bash
   docker-compose up --build
   ```

7. Open a browser and navigate to:

   ```
   http://localhost:8080
   ```

---

## Notes:
- Ensure **Docker Desktop** and **WSL2** are running properly before starting.
- If any issues arise, verify the dependencies and configurations in your environment.
