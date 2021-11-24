# sqlmodel-abstraction

An exploration of ideas for abstracting generation of SQLModel objects + FastAPI endpoints.

# 🤩 Motivation

[SQLModel](https://sqlmodel.tiangolo.com) is an elegant and intuitive package for building Pydantic-parsed SQL databases with a FastAPI interface.

We (core developers of [Pangeo Forge](https://pangeo-forge.readthedocs.io/en/latest/)) are exploring SQLModel for implementing [a database + API for that project](https://github.com/pangeo-forge/roadmap/pull/31).

In the course of prototyping, I ([@cisaacstern](https://github.com/cisaacstern)) came to wonder if introducing an abstraction/convenience layer on top of some of SQLModel's core functionality might make it easier to develop our application. This repo is an experimental implemention of that convenience layer. 

# 🔧 Setup

## Clone repo & install dependencies

1. Clone this repo and `cd` into it
2. Create and activate a new virtual environment with Python >= 3.6, < 3.10 
3. From the repo root, install project dependencies with `pip install -r requirements.txt`

## Confirm tests pass

From the repo root, run

```
$ pytest
```

to confirm that the project passes its tests in your local environment.

# 🤝 Same tests as tutorial

Importantly, in this repo _**the tests are identical**_ to [the tests in the SQLModel docs tutorial](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#add-the-rest-of-the-tests).

As such, the abstracted approach proposed here passes all of the same tests that the official tutorial example does.

# 📝 What is changed?

You will note that at 40 lines of code, this repo's [`main.py` module](https://github.com/cisaacstern/sqlmodel-abstraction/blob/main/project/main.py) is less than half as long as the 107-line [`main.py` module in the docs tutorial](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#fastapi-application) (also copied [here](https://github.com/cisaacstern/sqlmodel-abstraction/blob/baseline/project/main.py)).

> A full diff between the tutorial's `main.py` and this repo's main module is viewable [on GitHub here](https://github.com/cisaacstern/sqlmodel-abstraction/compare/baseline..main#diff-31264996fec2c210ab27c184fa7c2e98c35b245010e68cfacdb381f28121e7b9).

In brief, the conciseness gains in this repo's `main.py` are acheived via the addition of two objects in a new `abstractions.py` module:

- [**`MultipleModels`**](https://github.com/cisaacstern/sqlmodel-abstraction/blob/5909147685612c3a29faebcfb0332911d47a94ca/project/abstractions.py#L13): A dataclass that generates classes for the [multiple models with inheritance](https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/#multiple-models-with-inheritance) SQLModel design pattern and places them alongside a specified API endpoint path. This class requires a base model and a response (i.e. reader) model as input, and generates the remaining classes from these two in `__post_init__`. Theoretically, the response model can be deterministically generated from the base model as well (it requires only the addition of a required `id` field). I have not included this feature, however, because I'm not sure if there is a concise way to specify additional required (non-default) fields on a derived class using Python's built-in `type()` or `types.new_class()`.
- [**`RegisterEndpoints`**](https://github.com/cisaacstern/sqlmodel-abstraction/blob/5909147685612c3a29faebcfb0332911d47a94ca/project/abstractions.py#L129): This dataclass takes a `MultipleModels` instance (along with a `FastAPI` instance and `get_session` callable) as input, and from these automatically registers create, read, update, and delete (CRUD) endpoints for the `MultipleModels` instance with the `FastAPI` application instance.

> `register_endpoints` is a convenience function wrapping `RegisterEndpoints`, which is how this object is instantiated within `main.py`

We will greatly appreciate any feedback about potential issues which may arise if we opt to run this approach in production. Are there edge cases, not covered by the tutorial tests, where this style may falter? How might these abstractions be improved or refactored for increased reliability and/or readability? Thank you in advance for your consideration and feedback.
