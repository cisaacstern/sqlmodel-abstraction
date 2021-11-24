# sqlmodel-abstraction

An exploration of ideas for abstracting generation of SQLModel objects + FastAPI endpoints.

# Motivation

[SQLModel](https://sqlmodel.tiangolo.com) is an elegant and intuitive package for building Pydantic-parsed SQL databases with a FastAPI interface.

We (core developers of [Pangeo Forge](https://pangeo-forge.readthedocs.io/en/latest/)) are exploring SQLModel for implementing [a database + API for that project](https://github.com/pangeo-forge/roadmap/pull/31).

In the course of prototyping, I (@cisaacstern) came to wonder if introducing an abstraction/convenience layer on top of some of SQLModel's core functionality might make it easier to develop our application. This repo is an experimental implemention of that convenience layer. 

# Setup

## Clone repo & install dependencies

1. Clone this repo and `cd` into it
2. Create and activate a new virtual environment with Python >= 3.6, < 3.10 
3. From the repo root, run `pip install -r requirements.txt` to install project dependencies

## Confirm `main` tests pass

1. Note that `project/main.py` is copied directly from the the SQLModel docs [tutorial project](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#fastapi-application), and that `project/test_main.py` is copied directly from the SQLModel docs [tutorial tests](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#add-the-rest-of-the-tests).

2. From the repo root on branch `main`, run `pytest` to confirm that the tutorial project passes its tests in your local environment. (Further detail on running the tests [here](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#run-the-tests).)

## Re-run tests on `abstraction` branch

1. Run `git checkout abstraction` to checkout the abstractions proposed by this repo
2. Run `git diff --name-only main abstraction` and note that _**the tests are identical**_ between the `main` and `abstraction` branches; the only changed code is in the `project/main.py` module, and the added `project/abstractions.py` module.
3. From the repo root on branch `abstraction`, run `pytest` and observe that this abstracted approach passes the same tests as the `main` branch does.

# What has changed?

You will note that the `project/main.py` module has fewer lines of code on branch `abstraction` than on branch `main`. The full diff between these branches is viewable [on GitHub here](https://github.com/cisaacstern/sqlmodel-abstraction/compare/main..abstraction). In brief, the conciseness gains in `project/main.py` are acheived via the addition of two new objects in `project/abstractions.py`:

- **`MultipleModels`**: A dataclass that generates classes for the [multiple models with inheritance](https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/#multiple-models-with-inheritance) SQLModel design pattern and places them alongside a specified API endpoint path. This class requires a base model and a response (i.e. reader) model as input, and generates the remaining classes from these two in `__post_init__`. Theoretically, the response model can be deterministically generated from the base model as well (it requires only the addition of a required `id` field). I have not included this feature, however, because I'm not sure if there is a concise way to specify additional required (non-default) fields on a derived class using Python's built-in `type()` or `types.new_class()`.
- **`RegisterEndpoints`**: This dataclass takes a `MultipleModels` instance (along with a `FastAPI` instance and `get_session` callable) as input, and from these automatically registers create, read, update, and delete (CRUD) endpoints for the `MultipleModels` instance with the `FastAPI` application instance.

> `register_endpoints` is a convenience function wrapping `RegisterEndpoints`, which is how this object is instantiated within `project/main.py`

We will greatly appreciate any feedback about potential issues which may arise if we opt to run this approach in production. Are there edge cases, not covered by the tutorial tests, where this style may falter? How might these abstractions be improved or refactored for increased reliability and/or readability? Thank you in advance for your consideration and feedback.
