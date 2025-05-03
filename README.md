# notepadpp_updater

## Project Overview

The Notepad++ Updater is a Python utility designed to check for the latest Notepad++ releases, compare them with the installed version, and perform silent updates if necessary. It ensures that users always have the latest version of Notepad++ without manual intervention.

## Installation Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/rkapril/notepadpp_updater.git
   cd notepadpp_updater
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   ```bash
   source .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

To run the updater:

```bash
python run_updater.py
```
or 

Run `run.bat`

To run tests:

```bash
pytest
```

## Design Decisions

- **Modular Structure**: The project is organized into modules (elevate, installer, updater) to separate concerns and enhance maintainability.
- **Silent Installation**: Utilizes Notepad++'s silent installer for seamless updates.
- **Registry Access**: Checks Windows registry to determine the installed version of Notepad++.

## Testing Approach

- **Unit Tests**: Each module has corresponding test cases to validate functionality.
- **Mocking**: External dependencies like registry access and HTTP requests are mocked to ensure tests are isolated and reliable.

## Linting and Type Checking

- **Flake8**: Ensures code style consistency.
- **Mypy**: Performs static type checking.
- **Black**: Automatically formats code to adhere to PEP 8 standards.
- **Isort**: Organizes imports alphabetically and groups them logically.

To run linting and type checks:

```bash
flake8
mypy src
black --check .
isort --check-only .
```

## Summary:

The approach to this project involved creating a Python utility (notepadpp_updater) to manage the installation and updating of Notepad++ on Windows systems. The utility includes several key modules to handle specific tasks like checking for the installed version of Notepad++, downloading the latest version, and performing silent updates. The project was organized into logical modules for maintainability, including elevate, installer, updater, and registry.

For testing and quality assurance, I integrated tools like pytest, flake8, mypy, black, and isort to enforce code quality standards, perform type checking, and ensure consistent formatting. Configuration files (pyproject.toml, .flake8, etc.) were included to set up and automate these tools.

The overall goal was to ensure the utility was reliable, maintainable, and automated, including automated tests and checks for both functionality and code quality.

## Challenges Faced:

**Configuration Integration:**
Integrating all the linting, type-checking, and code-formatting tools (Flake8, Mypy, Black, Isort) into the pytest workflow posed a challenge due to compatibility and the required configuration. Ensuring that each tool was set up with the correct configuration options in pyproject.toml and worked together seamlessly required troubleshooting and testing of the individual tools before combining them.

**Error Handling and Robustness:**
Handling potential errors in the installer.download_installer method and ensuring that all errors were appropriately captured and raised as exceptions during tests was tricky. I had to simulate various network errors to ensure that the program could fail gracefully, which required setting up comprehensive error handling both in the application code and the corresponding tests.
