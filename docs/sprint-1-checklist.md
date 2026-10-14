# Sprint 1 Setup Checklist — IDSS

## 1. KML and GIS Inspection

- [x] Locate the original canal infrastructure KML.
- [x] Open the original KML in QGIS.
- [x] Record geometry elements, CRS, and bounding box.
- [x] Load the manually drawn boundary alongside the infrastructure.
- [x] Calculate and record the provisional polygon area.
- [x] Save the QGIS project as `idss-canal-boundary.qgz`.
- [ ] Validate that the manually drawn polygon represents the intended irrigation command area.

## 2. Development Environment

- [x] Verify Python availability and version.
- [x] Verify Git availability and version.
- [x] Verify Docker installation and runtime using `hello-world`.
- [x] Check available disk space.
- [x] Review the existing project README and Python version requirements.
- [ ] Install and verify project dependencies using the documented setup instructions.

## 3. Git and Repository Setup

- [x] Clone the shared GitHub repository.
- [x] Create a local `develop` branch.
- [x] Confirm write access to the shared GitHub repository.
- [x] Commit the setup documentation.
- [x] Push the `develop` branch to GitHub.
- [x] Verify the branch and commit on GitHub.

## 4. Documentation

- [x] Create `docs/kml-inspection.md`.
- [x] Create `docs/setup-prerequisites.md`.
- [ ] Create this Sprint 1 checklist.
- [ ] Review documentation for accuracy and consistency.
- [ ] Record unresolved blockers in the team's issue tracker.

## 5. Known Limitations and Blockers

- The manually drawn polygon area is approximately 174.875 km², but its suitability as the actual irrigation command area remains unverified.
- The project dependency installation and application tests have not yet been verified on this workstation.
- The `develop` branch exists locally; publication to the shared GitHub repository is pending.

## 6. Completion Criteria

This setup task can be closed when all acceptance criteria have been verified, the required documentation is committed, and any remaining blockers are recorded and accepted by the team.