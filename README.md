# Selenium-Pytest Automation for Stellar Burgers Website

## Overview
This project contains automated tests for the Stellar Burgers website (https://stellarburgers.nomoreparties.site/). The tests are written using Selenium WebDriver and Pytest. The main goal of the tests is to verify the functionality of the website, such as registration, login, navigating through the site, and ensuring the UI behaves as expected.

## Dependencies

- Python 3.x
- Selenium WebDriver
- Pytest

## Project Structure
- `tests/`: Directory containing all the test files.
- `Locators.py`: File containing all the locators used in the tests.
- `conftest.py`: File containing setup code, such as fixtures, for the tests.
- `.gitignore`: File telling git which files and directories to ignore.
- `README.md`: This file, explaining the project setup and structure.

## Additional Information
- The tests are designed to run on both Chrome and Firefox, but are configured to run on Chrome by default.
- The `conftest.py` file contains a fixture for initializing and tearing down the WebDriver.
- The `Locators.py` file contains the locators for the web elements in a centralized location, making the tests easier to maintain.
