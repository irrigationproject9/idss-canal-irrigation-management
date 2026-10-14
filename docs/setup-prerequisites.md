# Development Environment Verification — IDSS

## Purpose

Record the development prerequisites verified on the local Ubuntu workstation for the IDSS setup task. For installation and application setup instructions, refer to the repository's `README.md`.

## Verified Environment

| Item | Observed result |
|---|---|
| Operating system | Ubuntu 26.04.1 LTS |
| Python | 3.14.4 |
| Git | 2.53.0 |
| Docker | 29.1.3 |
| Docker Compose | 2.40.3 |
| Available disk space | Approximately 112 GB |

## Verification Results

- Python and Git are installed and available.
- Docker is installed.
- `sudo docker run hello-world` completed successfully.
- Available disk space was checked.
- The installed Python version matches the Python 3.14 requirement declared by the repository.

## Outstanding Checks

- Install project dependencies using the existing README instructions.
- Run the application and its tests.
- Record any setup failures as blockers.

## Reference

See `README.md` for software installation, environment configuration, dependency installation, application startup, health checks, and Git workflow instructions.