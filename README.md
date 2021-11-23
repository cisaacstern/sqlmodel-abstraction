# sqlmodel-abstraction

Exploring ideas for abstracting SQLModel object generation.

## Setup

1. Clone this repo and `cd` into it
2. Create and activate a new virtual environment with Python >= 3.6
3. From the repo root on branch `main`, run `pip install -r requirements.txt` to install project dependencies

## Confirm `main` tests pass

1. On the `main` branch, note that the `projects/main.py` module is the same as the code provided in https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#fastapi-application, and the `projects/test_main.py` module is the same as the code provided in https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#add-the-rest-of-the-tests.

2. From the repo root on branch `main`, run `pytest` to confirm that the baseline tests pass (as described in https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#run-the-tests)

## Run tests for `abstraction` branch

1. Run `git checkout abstraction` to checkout the abstractions proposed by this repo
2. Run `git diff baseline..abstraction` and note that the tests are identical to the baseline approach.
3. From the repo root on branch `abstraction`, run `pytest` and observe that these absractions pass the same tests.

## What has changed?

- **`MultipleModels` object**: Contains **factory functions**.
- **`GenerateEndpoints` object**