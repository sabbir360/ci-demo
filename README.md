# Overview
  This project demonstrated how can we go for a CI (Continuous Integration) using python and CircleCI.

## How to use this project 
  - Install python 3.11
  - Install virtualenv pip package using `pip install virtualenv`
  - Create a virtual environment using `virtualenv venv` and load
    - For Mac/Linux `source venv/bin/activate`
    - Windows `venv\Script\activate`
  - Install dependencies `pip install -r requirements`
  - For 
    - PEP8 standard check using flake8 `flake8 --statistics`
    - Test and Coverage `pytest -v --cov=calculator`
  - For circle CI integration visit [CircleCI](http://circleci.com) and connect your github repository