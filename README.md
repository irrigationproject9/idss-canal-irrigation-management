# IDSS Backend - Canal Irrigation Management

Intelligent Decision Support System (IDSS) backend application for satellite-driven crop intelligence and canal water allocation.

---

## Team Onboarding Guide (Ubuntu / Linux)

### 1. Prerequisites
Before cloning and setting up the project, ensure your Ubuntu machine has the necessary system-level geospatial C-libraries installed:

```bash
sudo apt update
sudo apt install -y gdal-bin libgdal-dev libgeos-dev libproj-dev python3-dev build-essential
```

---

### 2. Installation & Local Setup

#### Step 1: Clone the Repository
Clone the repository using SSH:
```bash
git clone git@github.com:irrigationproject9/idss-canal-irrigation-management.git
cd idss-canal-irrigation-management
```

#### Step 2: Set Up Environment Variables
Copy the example configuration file to create your local `.env`:
```bash
cp .env.example .env
```
*(Update the `.env` file with your local database credentials or API keys as needed).*

#### Step 3: Install `uv` (Package & Environment Manager)
If you don't have `uv` installed, install it using the official script:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

#### Step 4: Sync Environment & Install Dependencies
Use `uv sync` to automatically create the virtual environment (`.venv/`) and install all lockfile dependencies:
```bash
uv sync
```

#### Step 5: Activate Virtual Environment
```bash
source .venv/bin/activate
```
*Verification:* Run `which python` to verify that it points to `.venv/bin/python`.

---

### 3. Running the Application

Start the FastAPI development server with hot-reloading:
```bash
uv run uvicorn app.main:app --reload
```

---

### 4. Verify System Health

Verify that the server and geospatial modules are running correctly by calling the health endpoint:
```bash
curl http://127.0.0.1:8000/health
```

Expected Response:
```json
{
  "status": "healthy",
  "geospatial_engine": "operational"
}
```

---

### 5. Git & Workflow Standards

- Always pull the latest changes before starting work:
  ```bash
  git pull origin main
  ```
- Use descriptive commit messages following Conventional Commits (e.g., `feat: add postgis connection`, `fix: resolve geopandas crs issue`).
