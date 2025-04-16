# Selenium + Pytest Web Automation Framework

Scallable web automation framework build with Selenium, Pytest using Page Object Model

## Project structure

```
root/
├── README.md                           # Project documentation
├── requirements.txt                    # Required dependencies
├── Dockerfile                          # Docker image file
└── app/                                # Testing app directory
    │
    ├── config/                         # Shared configurations & driver setup
    │   ├── config.ini                  # Stored data (eg. passwords, api keys) - can be replaced with ENV variables
    │   └── driver_setup.py             # WebDriver fixtures
    │
    ├── logs/                           # Log files
    │   └── tests.log                   # Saved logs
    │
    ├── reports/                        # Captures
    │   ├── screenshots                 # Webdriver screenshots
    │   └── videos                      # Webdriver videos
    │
    ├── pages/                          # Page Object Model classes
    │   ├── BasePage.py                 # Common utilities (switching tabs, element awaits)
    │   └── HomePage.py                 # Page specific utilities (page locators, action methods)
    │
    └── tests/                          # Test cases
        ├── test_home.py                # Main page example test
        └── conftest.py                 # Delegates to driver_setup
```

## Installation

Create docker container or use venv to test locally

Install using:

- Docker (recommended)

```
git clone https://github.com/KacperMrochen/selenium.git
docker run --rm selenium-pytest
```

- venv (local use)

1. Create virtual environment and install dependencies

```
git clone https://github.com/KacperMrochen/selenium.git
cd selenium
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run tests

```
pytest
```
