# SymptomSurveyNoMore

This script will automatically fill out UCLA's daily Covid-19 symptom monitoring survey.

## Prerequisites

A ```credentials.txt``` must be provided in the root directory of the repo.
The file should contain your MyUCLA username on the first line, and your MyUCLA password on the second line.

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
