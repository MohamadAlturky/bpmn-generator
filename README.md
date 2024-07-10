# BPMN Generator

## Dev Plan

> we have two essential branches

- main
- dev

the dev branch is the place for continuous integration.

the main branch is always production ready it is the place for continuous depoyment.

## activate the virtual env

```bash

py -m venv ./venv

.\venv\Scripts\activate

pip install -r requirements.txt
```

## sync the packages

```bash
pip freeze > requirements.txt
```
