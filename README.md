# SymptomSurveyNoMore

This script will automatically fill out UCLA's daily Covid-19 symptom monitoring survey.

## Prerequisites

Program expects a `.env` file with the following format:
```
UCLA_USER=
UCLA_PASS=
```

Chromedriver is required for instantiating the selinium webdriver.
Chromedriver can be downloaded [here](https://sites.google.com/chromium.org/driver/downloads).
More information about selinium's requirements can be found [here](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver).

## Usage

After cloning the git repository, run the following commands:

(For first time `pipenv` use)

```bash
pip install pipenv
```

Followed by:

```bash
cd SymptomSurveyNoMore
pipenv install
```
