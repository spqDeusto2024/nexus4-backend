Execution
=========

To execute this project, you need to have the following installed:

- Docker Desktop
- WSL2 (Windows Subsystem for Linux 2)
- Node.js

To run the project, follow these steps:

1. Clone the repositories `nexus4-backend` and `nexus4-frontend` to your WSL2 machine.
2. Open a terminal and navigate to the root of the project `nexus4-backend`.
3. Run the following command:

   .. code-block:: bash

      ./build.sh

4. Once the build is complete, run the following command:

   .. code-block:: bash

      docker-compose up

5. Open a new terminal and navigate to the root of the project `nexus4-frontend`.
6. Run the following command:

   .. code-block:: bash

      docker-compose up --build

7. Open a browser and navigate to `http://localhost:8080`.
